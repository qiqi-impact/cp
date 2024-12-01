from functools import cache
from collections import defaultdict, deque
import math

d = defaultdict(int)

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        a = [int(x) for x in l.split(',')]
        for x in a: d[x] += 1

for i in range(256):
    nd = defaultdict(int)
    for k in d:
        if k == 0:
            nd[6] += d[k]
            nd[8] += d[k]
        else:
            nd[k-1] += d[k]
    d = nd

print(sum(d.values()))