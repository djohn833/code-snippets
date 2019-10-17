def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
vals = {}
vals[(0, 0)] = 1

p = (0, 0)
d = 0

for i in range(2, 4000):
    nextd = (d + 1) % 4
    nextp = add(p, deltas[nextd])
    if nextp in vals:
        nextd = d
        nextp = add(p, deltas[nextd])
    vals[nextp] = i
    d, p = nextd, nextp

knight = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

p = (0, 0); visited = set([(0, 0)]); visitedNums = [1]

while True:
    minNum = 999999999
    canMove = False
    for d in knight:
        nextp = add(p, d)
        if vals[nextp] < minNum and nextp not in visited:
            canMove = True
            minNum = vals[nextp]
            minNextP = nextp
    if not canMove:
        print('Stuck at %d' % vals[p])
        break
    p = minNextP
    visited.add(p)
    visitedNums.append(vals[p])

