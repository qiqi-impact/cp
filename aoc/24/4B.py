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
R, C = len(lines), len(lines[0])
ret = 0
for i in range(1, R-1):
    for j in range(1, C-1):
        if lines[i][j] != 'A':
            continue
        r = 0
        for a, b in [[[-1,-1], [1,1]], [[-1,1], [1,-1]]]:
            ax = a[0] + i
            ay = a[1] + j
            bx = b[0] + i
            by = b[1] + j
            r += ((lines[ax][ay] == 'S' and lines[bx][by] == 'M') or (lines[ax][ay] == 'M' and lines[bx][by] == 'S'))
        if r == 2:
            ret += 1

print(ret)
