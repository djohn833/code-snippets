#!/bin/python
from itertools import *

def assoc():
    for ff, ft, tf, tt in product([False, True], repeat=4):
        def op(x, y):
            if x:
                return tt if y else tf
            return ft if y else ff
        
        for x, y, z in product([False, True], repeat=3):
            xy = op(x, y)
            yz = op(y, z)
            xy_z = op(xy, z)
            x_yz = op(x, yz)
            if xy_z != x_yz:
                #print(x, y, z, xy, yz, xy_z, x_yz, ff, ft, tf, tt) 
                print(ff, ft, tf, tt) 
                #print(locals())

if __name__ == '__main__':
    assoc()

