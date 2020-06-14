#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import os
import os.path
from PIL import Image
import re
import pyautogui
import time
from tqdm import tqdm

winLeft = 8
winTop = 22

neko = Image.open('neko.png')

whiteColor = (255, 255, 255)

print('Loading font')
fontArray = np.load('fontdata.npy')
print('Font loaded')

def calibrate():
    global winLeft, winTop
    loc = pyautogui.locateOnScreen(neko)
    winLeft, winTop = loc.left, loc.top

def captureWindow():
    return pyautogui.screenshot(region=(winLeft, winTop, 643, 450))

def parseText(textbox, debug=False):
    px = textbox.load()

    pxArray = np.empty((16, 16))
    sjisText = bytearray()

    text = ''
    charNotFound = False

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
            if 0x7f <= coord2 < 0x9f:
                coord2 += 1
            sjisText = bytearray([coord1, coord2])
            try:
                char = sjisText.decode('shiftjis')
            except:
                if (coord1, coord2) == (0x86, 0x9d):
                    char = "\u300d" # Right corner bracket
                elif (coord1, coord2) == (0x86, 0x99):
                    char = "\u300b" # Right double angle bracket
                else:
                    char = "\u25a1" # White square
                    charNotFound = True

            if debug or char == "\u25a1":
                print('%d %d %d %d 0x%02x%02x %04x %d' % (j, i, minIndex[0], minIndex[1], coord1, coord2, ord(char), bestScore))
            text += char

    # Replace trailing spaces and punctuation incorrectly matched due to the text background
    text = re.sub(r"(\s|\u2032|\u25a1|\u309c|\uff0c|\uff40)*$", '', text)

    return text, charNotFound

def captureScreen():
    global window
    
    window = captureWindow()
    print('Screenshot captured')
    #window = Image.open('ss2.png')

def makeImageFilename(filename):
    ts = time.strftime("%Y%m%d-%H%M%S")
    basename = os.path.basename(filename)
    splitext = os.path.splitext(basename)
    return 'images/' + splitext[0] + ' ' + ts + '.png'

def captureScene(filename):
    captureScreen()
    
    scene = window.crop((97, 67, 545, 339))
    imageFilename = makeImageFilename(filename)
    scene.save(imageFilename)

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"<img src=\"{imageFilename}\" />\n")

def captureAndParse(filename, debug=False):
    global textbox

    captureScreen()
    
    textbox = window.crop((65, 355, 577, 440))
    #textbox.save('ss4.png')
    #textbox = Image.open('ss4.png')

    text, charNotFound = parseText(textbox, debug)
    #print(text)

    imageFilename = makeImageFilename(filename)

    if charNotFound:
        textbox.save(imageFilename)

    with open(filename, 'a', encoding='utf-8') as f:
        if charNotFound:
            f.write(f"<img src=\"{imageFilename}\" />\n")
        f.write('<p>' + text + "</p>\n")
        

if __name__ == '__main__':
    calibrate()
