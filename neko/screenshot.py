#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import os
from PIL import Image
import re
import pyautogui
from tqdm import tqdm

winLeft = 8
winTop = 22

neko = Image.open('neko.png')

whiteColor = (255, 255, 255)

fontArray = np.load('fontdata.npy')

def calibrate():
    global winLeft, winTop
    loc = pyautogui.locateOnScreen(neko)
    winLeft, winTop = loc.left, loc.Top

def captureWindow():
    return pyautogui.screenshot(region=(winLeft, winTop, 643, 450))

#calibrate()
#window = captureWindow()
#window = Image.open('ss2.png')
#textbox = window.crop((65, 355, 577, 440))
#textbox.save('ss3.png')
textbox = Image.open('ss3.png')
px = textbox.load()

pxArray = np.empty((16, 16))
sjisText = bytearray()

text = ''

for j in range(0, 3):
    for i in range(0, 32):
        for k in range(0, 16):
            for m in range(0, 16):
                pxArray[k, m] = px[i*16 + k, j*20 + m] == whiteColor

        resultArray = np.logical_xor(fontArray, pxArray)
        resultArray = np.sum(resultArray, axis=(-1, -2))
        minIndex = np.unravel_index(np.argmin(resultArray), resultArray.shape)
        bestScore = resultArray[minIndex]
        coord1 = 0x81 + (minIndex[0] // 2)
        coord2 = (0x40 if minIndex[0] % 2 == 0 else 0x9f) + (minIndex[1])
        if 0x80 <= coord2 < 0x9f:
            coord2 += 1
        sjisText = bytearray([coord1, coord2])
        #print('%d %d 0x%02x%02x %d' % (j, i, coord1, coord2, bestScore))
        text += sjisText.decode('shiftjis')

# Replace trailing spaces and punctuation incorrectly matched due to the text brackground
text = re.sub(r"(\s|\u2032)*$", '', text)

print(text)

with open('text.txt', 'w', encoding='utf-8') as f:
    f.write(text)
