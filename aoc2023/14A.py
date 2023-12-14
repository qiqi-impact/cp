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
R, C = ln, len(lines[0])


grid = [[None for _ in range(C)] for _ in range(R)]
ret = 0
for j in range(C):
    ct = 0
    q = R
    for i in range(R):
        v = lines[i][j]
        if v == '#':
            q = R-i-1
        elif v == 'O':
            ct += q
            q -= 1
    ret += ct
print(ret)