from functools import cache
from collections import defaultdict, deque
import math

d = defaultdict(int)

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        a = [int(x) for x in l.split(',')]
        for x in a: d[x] += 1

ret = 1e18
for k in d:
    cur = 0
    for x in d:
        cur += d[x] * abs(x - k)
    ret = min(cur, ret)

print(ret)