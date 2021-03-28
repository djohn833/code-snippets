#!/bin/python
from itertools import product

opNames = {
    (False, False, False, False): 'Constant False',
    (False, False, False, True): 'AND',
    (False, False, True, False): 'NOT p Implies q',
    (False, False, True, True): 'p',
    (False, True, False, False): 'NOT p Implied By q',
    (False, True, False, True): 'q',
    (False, True, True, False): 'XOR',
    (False, True, True, True): 'OR',
    (True, False, False, False): 'NOR',
    (True, False, False, True): 'XNOR',
    (True, False, True, False): 'NOT q',
    (True, False, True, True): 'p Implied by q',
    (True, True, False, False): 'NOT p',
    (True, True, False, True): 'p Implies q',
    (True, True, True, False): 'NAND',
    (True, True, True, True): 'Constant True'
}

isCommutative = {}
isAssociative = {}

def makeOp(ff, ft, tf, tt):
    return lambda x, y: (tt if y else tf) if x else (ft if y else ff)

def truthTable(n):
    return product([False, True], repeat=n)

def commutative():
    for ff, ft, tf, tt in truthTable(4):
        op = makeOp(ff, ft, tf, tt)

        found = False

        x, y = False, True
        xy = op(x, y)
        yx = op(y, x)
        if xy != yx:
            print(f'Not commutative: {opNames[(ff, ft, tf, tt)]} {x} * {y} != {y} * {x}')
            found = True
        
        isCommutative[(ff, ft, tf, tt)] = not found
        if not found:
            print(f'Commutative: {opNames[(ff, ft, tf, tt)]}')

def associative():
    for ff, ft, tf, tt in truthTable(4):
        op = makeOp(ff, ft, tf, tt)

        found = False

        for x, y, z in truthTable(3):
            xy_z = op(op(x, y), z)
            x_yz = op(x, op(y, z))
            if xy_z != x_yz:
                print(f'Not associative: {opNames[(ff, ft, tf, tt)]} ({x} * {y}) * {z} != {x} * ({y} * {z})')
                found = True

        isAssociative[(ff, ft, tf, tt)] = not found
        if not found:
            print(f'Associative: {opNames[(ff, ft, tf, tt)]}')

if __name__ == '__main__':
    commutative()
    associative()
    for key in truthTable(4):
        print(f'{opNames[key]}\t{isCommutative[key]}\t{isAssociative[key]}')
