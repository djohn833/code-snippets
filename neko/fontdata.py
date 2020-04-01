#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
from tqdm import tqdm

print('Loading font')

font = Image.open('font.inv.bmp')
fontPx = font.load()

fontArray = np.empty((92, 94, 16, 16), bool)

for i in tqdm(range(16, 1488, 16)):
    for j in range(528, 2032, 16):
        for k in range(0, 16):
            for m in range(0, 16):
                fontArray[(i-16) // 16, (j-528) // 16, k, m] = fontPx[i + k, j + m]

print('Font loaded')

np.save('fontdata', fontArray)