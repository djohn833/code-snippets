from math import e, exp

x = exp(1/e)
N = 100_000

a = 1
for i in range(1, N + 1):
  a = x ** a
  #print(i, a)

print(i, a)
