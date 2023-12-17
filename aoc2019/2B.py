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
# ln = len(lines)

def f(i, j):
    l = ints(lines[0], ',')
    l[1] = i
    l[2] = j

    pt = 0
    while 1:
        v = l[pt]
        if v == 99:
            break
        if v == 1:
            a, b, c = l[pt+1], l[pt+2], l[pt+3]
            l[c] = l[a] + l[b]
        else:
            a, b, c = l[pt+1], l[pt+2], l[pt+3]
            l[c] = l[a] * l[b]
        pt += 4
    print(i, j, l[0])

for i in range(1, 10):
    for j in range(1, 10):
        f(i, j)