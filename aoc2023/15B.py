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

def hsh(s):
    ret = 0
    for c in s:
        ret = (ret + ord(c))*17%256
    return ret

m = [[] for _ in range(256)]


l = lines[0].split(',')
for x in l:
    if x[-1] == '-':
        h = hsh(x[:-1])
        m[h] = [y for y in m[h] if y[0] != x[:-1]]
    else:
        a, b = x.split('=')
        h = hsh(a)
        b = int(b)
        f = 0
        for i in range(len(m[h])):
            if m[h][i][0] == a:
                m[h][i][1] = b
                f = 1
                break
        if not f:
            m[h].append([a, b])

ret = 0
for j, x in enumerate(m):
    for i, y in enumerate(x):
        ret += (i+1) * (j+1) * y[1]
print(ret)