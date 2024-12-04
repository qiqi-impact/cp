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

ls = [0] + sorted([int(x) for x in lines])
ls.sort()
print(ls)
od, td = 0, 1
for i in range(len(ls)-1):
    if ls[i+1] - ls[i] == 1:
        od += 1
    elif ls[i+1] - ls[i] == 3:
        td += 1
print(od * td)