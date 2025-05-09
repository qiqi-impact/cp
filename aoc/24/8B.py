from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def grabint(s, idx):
    cur = 0
    ln = 0
    for i in range(idx, len(s)):
        try:
            cur = 10 * cur + int(s[i])
        except:
            return cur, i
    return cur, len(s)

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

# dirmap = {
#     'R': [0, 1],
#     'L': [0, -1],
#     'U': [-1, 0],
#     'D': [1, 0],
# }
# L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
# DIR = [R, D, L, U]

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)

f = defaultdict(list)
an = set()

R, C = len(lines), len(lines[0])
for i in range(R):
    for j in range(C):
        v = lines[i][j]
        if v != '.':
            for (x, y) in f[v]:
                dx, dy = x - i, y - j

                cx, cy = i, j
                while 0 <= cx < R and 0 <= cy < C:
                    an.add((cx, cy))
                    cx -= dx
                    cy -= dy

                cx, cy = x, y
                while 0 <= cx < R and 0 <= cy < C:
                    an.add((cx, cy))
                    cx += dx
                    cy += dy

            f[v].append((i, j))
ret = 0
for x, y in an:
    if 0 <= x < R and 0 <= y < C:
        ret += 1
print(ret)