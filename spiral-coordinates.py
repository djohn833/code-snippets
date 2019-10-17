deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
vals = {}
vals[(0, 0)] = 1

p = (0, 0)
d = 0

for i in range(2, 4000):
    nextd = (d + 1) % 4
    nextp = (p[0] + deltas[nextd][0], p[1] + deltas[nextd][1])
    if nextp in vals:
        nextd = d
        nextp = (p[0] + deltas[nextd][0], p[1] + deltas[nextd][1])
    vals[nextp] = i
    d, p = nextd, nextp

knight = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

p = (0, 0); visited = set([(0, 0)]); visitedNums = [1]

while True:
    for d in knight:
        nextp = (p[0] + d[0], p[1] + d[1])
        if nextp not in visited:
            break
    else:
        print('Stuck at %d' % vals[p])
        break
    minNum = 999999999
    for d in knight:
        nextp = (p[0] + d[0], p[1] + d[1])
        if vals[nextp] < minNum and nextp not in visited:
            minNum = vals[nextp]
            minNextP = nextp
    p = minNextP
    visited.add(p)
    visitedNums.append(vals[p])

