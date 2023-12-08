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

d = {}
for l in lines[2:]:
    a, b = l.split(' = ')
    x, y = b[1:-1].split(', ')
    d[a] = [x, y]

cur = 'AAA'
ct = 0
inst = lines[0]
while cur != 'ZZZ':
    c = inst[ct%len(inst)]
    if c == 'L':
        cur = d[cur][0]
    else:
        cur = d[cur][1]
    ct += 1
print(d)
print(ct)
