from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math

lit = set()

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        if i == 0:
            code = l
        elif i >= 2:
            for j, c in enumerate(l):
                if c == '#':
                    lit.add((i-2, j))

outside_lit = (-1e9, 1e9, -1e9, 1e9)

def next(x, y):
    b = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = x+dx, y+dy
            b *= 2
            b += int((nx, ny) in lit or nx < outside_lit[0] or nx > outside_lit[1] or ny < outside_lit[2] or ny > outside_lit[3])
    return bool(code[b] == '#')

WINDOW = 2

for p in range(50):
    mnx, mxx, mny, mxy = 1e9, -1e9, 1e9, -1e9
    for (x, y) in lit:
        mnx = min(mnx, x)
        mny = min(mny, y)
        mxx = max(mxx, x)
        mxy = max(mxy, y)

    nl = set()
    for x in range(mnx - WINDOW, mxx + WINDOW + 1):
        for y in range(mny - WINDOW, mxy + WINDOW + 1):
            if next(x, y):
                nl.add((x, y))
    lit = nl

    if p%2 == 0:
        outside_lit = (mnx - WINDOW, mxx + WINDOW, mny - WINDOW, mxy + WINDOW)
    else:
        outside_lit = (-1e9, 1e9, -1e9, 1e9)

# print(sorted(lit))
print(len(lit))
