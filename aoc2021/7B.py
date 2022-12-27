from functools import cache
from collections import defaultdict, deque
import math

d = defaultdict(int)

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        a = [int(x) for x in l.split(',')]
        for x in a: d[x] += 1

ret = 1e18
for i in range(min(d.keys()), max(d.keys())+1):
    cur = 0
    for x in d:
        cur += d[x] * abs(x - i) * (abs(x - i) + 1) // 2
    # print(i, cur)
    ret = min(cur, ret)

print(ret)