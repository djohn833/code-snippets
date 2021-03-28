import numpy as np

def gcd(a, b):
  curr = np.array([a, 1, 0]) # a = 1*a + 0*b
  next = np.array([b, 0, 1]) # b = 0*a + 1*b

  while next[0] != 0:
    q = curr[0] // next[0]
    curr, next = next, curr - q * next

  if curr[0] < 0:
    curr *= -1

  return tuple(curr)
