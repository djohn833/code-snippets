import os
from PIL import Image
import pyautogui

winLeft = 8
winTop = 22

neko = Image.open('neko.png')
base = Image.open('base.png')
basePx = base.load()
font = Image.open('font.inv.bmp')
fontPx = font.load()

whiteColor = (255, 255, 255)
blackColor = (0, 0, 0)
grayColor = (128, 128, 128)
redColor = (255, 0, 0)

def calibrate():
        global winLeft, winTop
        loc = pyautogui.locateOnScreen(neko)
        winLeft = loc.left
        winTop = loc.top

def captureWindow():
        return pyautogui.screenshot(region=(winLeft, winTop, 643, 450))

def filterTextbox(textbox):
        global basePx
        
        px = textbox.load()

        matchesBase = True
        
        for i in range(0, textbox.size[0]):
                for j in range(0, textbox.size[1]):
                        if px[i, j] != whiteColor:
                                px[i, j] = blackColor
                        if basePx[i, j] == whiteColor and px[i, j] != whiteColor:
                                #matchesBase = False
                                #print("Doesn't match base.png: (%d, %d)" % (i % 2, j % 2))
                                break

        if matchesBase:
                for i in range(0, textbox.size[0]):
                        for j in range(0, textbox.size[1]):
                                if px[i, j] == whiteColor and basePx[i, j] == whiteColor:
                                        pass
                                        #px[i, j] = grayColor
                                        #px[i, j] = blackColor
                                        #px[i, j] = redColor
                                if (i + 1) % 16 == 0 or j + 1 in [16, 20, 36, 40, 56, 60, 76, 80]:
                                        pass
                                        #px[i, j] = redColor

def matchScore(c1, c2):
        score = 0
        for i in range(16):
                for j in range(16):
                        if (c1[i, j] == whiteColor and c2[i, j] == 0) or (c1[i, j] == blackColor and c2[i, j] == 255):
                                score += 1
        return score

def findMatch(x, y):
        #char = textbox.crop((x * 16, y * 16, x*16 + 16, y*20 + 16))
        #charPx = char.load()
        #char.save('char.png')
        bestScore = 16*16 # Complete mismatch
        numMatch = 0
        for i in range(16, 1488, 16):
                for j in range(528, 2032, 16):
                        score = 0
                        for k in range(0, 16):
                                for m in range(0, 16):
                                        p1 = px[x*16 + k, y*20 + m]
                                        p2 = fontPx[i + k, j + m]
                                        if (p1 == whiteColor and p2 == 0) or (p1 == blackColor and p2 == 255):
                                                score += 1
                        if score < bestScore:
                                bestScore = score
                                numMatch = 1
                                bestLoc = (i // 16, j // 16)
                        elif score == bestScore:
                                numMatch += 1
        return (bestLoc, bestScore, numMatch)

# notes
# columns:
# 01st 8140
# 02nd 819F
# 03rd 8240 (?)
# 04th 829F (?)
# 05th 8340
# 06th 839E
# 07th 8440 (?)
# 08th 849F (?)
# 09th 8540 starts with exclamation mark
# 10th 859F starts with period
# 11th 8640 starts with space then quote mark
# 12th 869F starts with 3 spaces then line
# 13th 8740 starts with 1 inside circle
# 14th 879F blank
# 15th 8840 blank
# 16th 889F start of kanji block
# 17th 8940 2nd column of kanji block
# 18th 899F 3rd column of kanji block
# 19th 8A40


# 19th 9040

# 部屋の中は暗い。長年の埃と脂が染み着いて大層な歴史を感じさせる。


#calibrate()
#window = captureWindow()
#window = Image.open('ss2.png')
#textbox = window.crop((65, 355, 577, 440))
#filterTextbox(textbox)
#textbox.save('ss3.png')
textbox = Image.open('ss3.png')

px = textbox.load()

sjisText = bytearray()

with open('text.txt', 'a', encoding='utf-8') as f:
        for j in range(0, 3):
                for i in range(0, 32):
                        bestLoc, bestScore, numMatch = findMatch(i, j)
                        #print('%d %d' % bestLoc)
                        coord1 = 0x81 + ((bestLoc[0]-1) // 2)
                        coord2 = (0x40 if bestLoc[0] % 2 == 1 else 0x9f) + (bestLoc[1] - 33)
                        if 0x80 <= coord2 < 0x9f:
                                coord2 += 1
                        sjisText = bytearray([coord1, coord2])
                        #sjisText.append(coord1)
                        #sjisText.append(coord2)
                        print('%d %d 0x%02x%02x %d %d' % (j, i, coord1, coord2, numMatch, bestScore))
                        #bestChar.save('match2.bmp')
                        #sjisText = b'\x%02x\x%02x' % (coord1, coord2)
                        f.write(sjisText.decode('shiftjis'))
                        f.flush()
