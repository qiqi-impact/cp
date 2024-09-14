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

l = []
with open("in") as f:
    for a in f.read().splitlines():
        l.append(a)

t = ints(colon(l[0]))
d = ints(colon(l[1]))

ret = 1
for r in range(len(t)):
    cur = 0
    for i in range(1, t[r]):
        dd = (t[r]-i)*i
        if dd > d[r]:
            cur += 1
    ret *= cur
print(ret)