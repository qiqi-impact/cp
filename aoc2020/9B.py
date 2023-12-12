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

l = [int(x) for x in l]

pre = 25
t = 15353384
# t = 127

j = 0
sm = 0
for i in range(ln):
    while j < len(l):
        if sm + l[j] <= t:
            sm += l[j]
            j += 1
            # print(sm, l[j])
        else:
            break
    # print(i, j, sm)
    if sm == t and j != i+1:
        print(i, j, sm, max(l[i:j]) + min(l[i:j]))
    sm -= l[i]