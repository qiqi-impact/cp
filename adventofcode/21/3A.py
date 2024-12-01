from functools import cache
from collections import defaultdict, deque
import math

N = 12

ret = 0
ll = [0] * N
ct = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        for j, c in enumerate(l):
            ll[j] += int(c)
        ct += 1

g, e = 0, 0
for j in range(N):
    g *= 2
    e *= 2
    if ll[j] * 2 > ct:
        g += 1
    else:
        e += 1

print(g*e)