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

ret = 0
for t in lines:
    tt = [ints(t)]
    while 1:
        q = []
        for i in range(len(tt[-1])-1):
            q.append(tt[-1][i+1] - tt[-1][i])
        if sum(q) == 0 and len(set(q)) == 1:
            tt.append(q)
            break
        tt.append(q)
    print(tt)
    cur = 0
    for i in range(len(tt)-1, -1, -1):
        cur += tt[i][-1]
        print(cur)
    ret += cur
print(ret)
