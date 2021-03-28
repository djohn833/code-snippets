import itertools
from z3 import *

a = Int('a')
b = Int('b')
c = Int('c')
d = Int('d')
e = Int('e')
f = Int('f')
g = Int('g')

s = Solver()

s.add(0 == a or a == 1)
s.add(0 == b or b == 1)
s.add(0 == c or c == 1)
s.add(0 == d or d == 1)
s.add(0 == e or e == 1)
s.add(0 == f or f == 1)
s.add(0 == g or g == 1)

s.add(a + b + c == 2)
s.add(a + d == 1)
s.add(d + e + f + g == 2)
s.add(c + g == 1)

print(s.check())
print(s.model())

