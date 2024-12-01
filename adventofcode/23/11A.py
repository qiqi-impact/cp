from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
ln = len(lines)

cr, cc = set(), set()
R, C = ln, len(lines[0])

items = []

for i in range(R):
    has = 0
    for j in range(C):
        if lines[i][j] == '#':
            items.append((i, j))
            has = 1
    if not has:
        cr.add(i)

for j in range(C):
    has = 0
    for i in range(R):
        if lines[i][j] == '#':
            has = 1
    if not has:
        cc.add(j)

N = 2

ii = []
for i, j in items:
    rr = 0
    for r in range(i):
        if r in cr:
            rr += N-1
    yy = 0
    for c in range(j):
        if c in cc:
            yy += N-1
    ii.append((i+rr, j+yy))

items = ii
print(items, cr, cc)

ret = 0
for i in range(len(items)):
    a, b = items[i]
    for j in range(i+1, len(items)):
        c, d = items[j]
        ret += abs(c-a) + abs(d-b)
print(ret)