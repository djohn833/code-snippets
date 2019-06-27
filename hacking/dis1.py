from struct import pack, unpack

def db(v):
  return pack("<B", v)

def dw(v):
  return pack("<H", v)

def dd(v):
  return pack("<I", v)

def dq(v):
  return pack("<Q", v)

def rb(v):
  return unpack("<B", v[0])[0]

def rw(v):
  return unpack("<H", v[:2])[0]

def rd(v):
  return unpack("<I", v[:4])[0]

def rq(v):
  return unpack("<Q", v[:8])[0]

startRopVma    = 0x80eb084
startRopOffset = 0xa2084
endRopOffset   = 0xbe130

with open('just-another-matryoshka-crackme', 'rb') as f:
	rop = f.read()[startRopOffset : endRopOffset]

dwords = []
for i in range(0, len(rop), 4):
	dwords.append(rd(rop[i:i+4]))

execCode = (0x08048000, 0x080bffff)
dataRef  = (0x080c0000, 0x081effff)

gadgets = set()

# pop instructions will move the next dword into the register
# they effectively store a constant into the register
def opcode_pop(fmt, dwords, i):
	return (1, fmt % dwords[i])

def opcode_load_pop(fmt, dwords, i):
	return (3, fmt % dwords[i + 3])

# Use "disass <addr>,+<length>" in gdb to disassemble arbitrary memory.
opcodes = {
0x080488d2: ('??ret 0x8d04', None),
0x08048e28: ('mov ecx, 0x%08x', opcode_pop),
0x08048e2d: ('mov ecx, [ecx]', None),
0x08048e30: ('mov eax, esi', None),
0x08048e33: ('mov esi, eax', None),
0x08048e36: ('mul ecx', None),
0x08048e39: ('int3', None),
0x08048e3b: ('xor eax, ecx', None),
0x08048e3e: ('or eax, ecx', None),
0x08048e41: ('mov [eax], ecx', None),
0x0804c2e4: ('xchg esp, eax', None),
0x08050780: ('call puts', None),
0x080537c0: ('movzx eax, byte ptr [eax]; mov ebx, 0x%08x', opcode_load_pop),
0x08055b22: ('mov [edx], ecx', None),
0x08056875: ('mov [eax+edx], cl', None),
0x08062c48: ('sub eax, ecx', None),
0x0806d551: ('call exit', None),
0x0806f80c: ('cmove eax, edx', None),
0x0806f96a: ('mov edx, 0x%08x', opcode_pop),
0x080a28ed: ('mov [edx], eax', None),
0x080a5ae0: ('mov eax, [eax+4]', None),
0x080bbef6: ('jmp 0x%08x', opcode_pop),
0x080bbf46: ('mov eax, 0x%08x', opcode_pop),
0x080bc936: ('mov eax, [eax]; mov ebx, 0x%08x', opcode_load_pop),
}

i = 0
while i < len(dwords):
	d = dwords[i]
	used = 0
   
	desc = '' 
	if execCode[0] <= d <= execCode[1]:
		desc = 'UNKNOWN GADGET'
		if d in opcodes and opcodes[d]:
			if opcodes[d][1]:
				used, desc = opcodes[d][1](opcodes[d][0], dwords, i + 1)
			else:
				desc = opcodes[d][0]
		else:
			gadgets.add(d)
	elif dataRef[0] <= d <= dataRef[1]:
		desc = 'data ref?'
    
	print('%.5x - VMA 0x%08x: 0x%08x %s' % (i, startRopVma + i*4, d, desc))
	i += used + 1

len(gadgets)
for g in sorted(gadgets):
	print('0x%08x' % g)

