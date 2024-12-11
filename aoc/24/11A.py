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

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)

l = ints(lines[0])
ct = defaultdict(int)
for x in l:
    ct[x] += 1
for i in range(25):
    nct = defaultdict(int)
    for x in ct:
        y = ct[x]
        t = str(x)
        if x == 0:
            nct[1] += y
        elif len(t) % 2 == 0:
            a, b = int(t[:len(t)//2]), int(t[len(t)//2:])
            nct[a] += y
            nct[b] += y
        else:
            nct[x * 2024] += y
    ct = nct
print(sum(ct.values()))
        