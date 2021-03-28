import cmath

def primRootUnity(n):
  if n == 1:
    return 1
  elif n == 2:
    return -1
  elif n == 4:
    return 1j
  else:
    return cmath.rect(1.0, 2*cmath.pi / n)

def FFT(L):
  n = len(L)
  if n == 1:
    return L
  L_odd, L_even = L[0::2], L[1::2]
  P_odd, P_even = FFT(L_odd), FFT(L_even)
  q = cmath.rect(1.0, 2*cmath.pi / n)
  q_i = 1
  p = [0] * n
  for i in range(n // 2):
    t = q_i * P_even[i]
    p[i] = P_odd[i] + t
    p[i + n//2] = P_odd[i] - t
    q_i *= q
  return p

def IFFT(L, q):
  n = len(L)
  if n == 1:
    return L
  L_odd, L_even = L[0::2], L[1::2]
  P_odd, P_even = IFFT(L_odd, q*q), IFFT(L_even, q*q)
  # print(P_odd, P_even)
  # q = cmath.rect(1.0, -2*cmath.pi / n)
  q_i = 1
  p = [0] * n
  for i in range(n // 2):
    t = q_i * P_even[i]
    p[i] = (P_odd[i] + t) / 2
    p[i + n//2] = (P_odd[i] - t) / 2
    q_i *= q
  return p

if __name__ == '__main__':
  print(FFT([5, 3, 2, 1]))
  print([x.real for x in IFFT([11, (3+2j), 3, (3-2j)], 1j)])
  print(FFT([5, 2]))
  print(IFFT([7, 3], -1))
  print(FFT([3, 1]))
  print(IFFT([4, 2], -1))
