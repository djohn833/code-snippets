import os
from PIL import Image
import pyautogui

winLeft = 8
winTop = 22

neko = Image.open('neko.png')
base = Image.open('base.png')
basePx = base.load()

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

calibrate()
window = captureWindow()
window = Image.open('ss2.png')
textbox = window.crop((65, 355, 577, 440))
filterTextbox(textbox)
textbox.save('ss3.png')
