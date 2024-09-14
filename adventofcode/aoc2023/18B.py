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

dirmap = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0],
}
L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

path = [(0, 0)]
cx, cy = 0, 0
border = 0
for l in lines:
    _,_,c = l.split(' ')
    b = int(c[2:-2], 16)
    a = DIR[int(c[-2])]
    dx, dy = a
    dx *= b
    dy *= b
    cx += dx
    cy += dy
    path.append((cx, cy))
    border += b
path.pop()

area = 0
for i in range(len(path)):
    a, b = path[(i-1)%len(path)]
    c, d = path[i]
    area += (a - c) * (b + d)
area //= 2
area = abs(area)

interior = area - border // 2 + 1
print(border, interior, border + interior)
