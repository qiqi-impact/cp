from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

ret = []
ct = 0
maps = []
r = []
with open("in") as f:
    for a in f.read().splitlines() + ['']:
        ct += 1
        if ct == 1:
            seeds = ints(colon(a))
            # print(seeds)
        elif a == '':
            maps.append(r)
            r = []
        elif ':' not in a:
            x, y, z = ints(a)
            r.append([y, y+z-1, x, x+z-1])
cur = seeds[:]
for m in maps:
    nc = []
    for x in cur:
        found = x
        for mm in m:
            if mm[0] <= x <= mm[1]:
                found = mm[2] - mm[0] + x
                break
        nc.append(found)
    cur = nc
print(min(cur))

