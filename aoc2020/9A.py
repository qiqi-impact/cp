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
ln = len(l)

pre = 25
for i in range(pre, ln):
    k = int(l[i])
    f = 0
    for x in l[i-pre:i]:
        for y in l[i-pre:i]:
            x = int(x)
            y = int(y)
            if x != y and x+y==k:
                f = 1
                break
        if f: break
    if not f:
        print(k)
        break

