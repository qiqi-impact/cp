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
ct = 1
r = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
        if 1 <= ct <= 2:
            q = a.split('+')
            adx = int(q[1].split(',')[0])
            ady = int(q[2])
            r.append([adx, ady])
        elif ct == 3:
            q = a.split('=')
            adx = int(q[1].split(',')[0])
            ady = int(q[2])
            r.append([adx, ady])
        ct = (ct + 1) % 4

import sys
sys.setrecursionlimit(1500)

y = 0
for i in range(0, len(r), 3):
    mn = math.inf
    t, v = r[i+2][0], r[i+2][1]
    for a in range(10**18):
        if t % r[i+1][0] == 0 and v % r[i+1][1] == 0:
            o, p = t // r[i+1][0], v // r[i+1][1]
            if o == p:
                mn = min(mn, 3 * a + o)
        t -= r[i][0]
        v -= r[i][1]
        if t < 0 or v < 0:
            break

    if mn < math.inf:
        y += mn

print(y)