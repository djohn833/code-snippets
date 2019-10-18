from math import *
from random import *

N = 1000000

def angle():
	return uniform(0, 2*pi)

def coord(t):
    return (cos(t), sin(t))

def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)

def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def distO(p):
    return sqrt(p[0] ** 2 + p[1] ** 2)


# Probability that three random points on a circle form a triangle that contains the center of the circle
n = 0
for i in range(N):
    b, c = sorted([angle() for j in range(2)])
    if b <= pi and c - b <= pi and (2*pi - c) <= pi:
        n += 1
print('Random points: %f' % (float(n) / N))


# Probability that a random chord is longer than the sides of an inscribed equilateral triangle.

# Method 1: Endpoints of chords are uniformly distributed on the circle.
# Because length (of the chord in particular) is invariant under rotation,
# rotate so that one point becomes (1, 0). Then pick the other end of the chord
# with a random angle [0, 2pi].
n = 0
for i in range(N):
    b, = [angle() for j in range(1)]
    if (2.0 * pi) / 3.0 <= b <= (4.0 * pi) / 3.0:
        n += 1
print('Random chord endpoints: %f' % (float(n) / N))

# Method 1a: Same uniform distribution of endpoints of chord, but check distance from the midpoint
# of the chord to the center of the circle instead.
n = 0
for i in range(N):
    b, = [angle() for j in range(1)]
    if distO(midpoint((1, 0), coord(b))) <= 0.5:
        n += 1
print('Random chord endpoints: %f' % (float(n) / N))

# Method 2: Midpoints of chords are "uniformly" distributed in the circle (by cartesian coordinates).
n = 0
for i in range(N):
    while True:
        p = [uniform(-1, 1) for j in range(2)]
        d = distO(p)
        if d < 1.0:
            break
    if d <= 0.5:
        n += 1
print('Random chord midpoints (by area): %f' % (float(n) / N))

# Method 3: Midpoints of chords are uniformly distributed by distance from the center of the circle.
n = 0
for i in range(N):
    d, = [uniform(0, 1) for j in range(1)]
    if d <= 0.5:
        n += 1
print('Random chord midpoints (by distance from center): %f' % (float(n) / N))

