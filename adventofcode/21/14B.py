from functools import cache
from collections import defaultdict, deque, Counter
import math

stage = 0
rules = {}
pairs = defaultdict(int)
ret = defaultdict(int)

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        if len(l) == 0:
            stage += 1
            continue
        if stage == 0:
            ret[l[0]] += 1
            ret[l[-1]] += 1
            for i in range(len(l)-1):
                pairs[l[i:i+2]] += 1
        if stage == 1:
            a, b = l.split(' -> ')
            rules[a] = [a[0]+b, b+a[1]]

for _ in range(40):
    np = defaultdict(int)
    for p in pairs:
        if p in rules:
            a, b = rules[p]
            np[a] += pairs[p]
            np[b] += pairs[p]
        else:
            np[p] += pairs[p]
    pairs = np

for p in pairs:
    ret[p[0]] += pairs[p]
    ret[p[1]] += pairs[p]

print((max(ret.values()) - min(ret.values())) // 2)