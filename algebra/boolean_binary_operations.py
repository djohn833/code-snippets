import itertools
from z3 import *

P = {
    (False, False): Bool('0 op 0'),
    (False, True ): Bool('0 op 1'),
    (True , False): Bool('1 op 0'),
    (True , True ): Bool('1 op 1')
}   

s = Solver()

for b in [False, True]:
    s.add(P[(b, b)] == b)

print(s.check())
print(s.model())

