from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math

p = []

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        p.append(int(l[-2:]))
score = [0, 0]

roll = defaultdict(int)
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            roll[i+j+k] += 1

@cache
def dp(left, t, pos):
    if left[0] == 0:
        return [1, 0]
    elif left[1] == 0:
        return [0, 1]
    ret = [0, 0]
    for k in roll:
        l = list(left)
        p = list(pos)
        p[t] = (p[t] - 1 + k) % 10 + 1
        l[t] = max(0, l[t] - p[t])
        a, b = dp(tuple(l), 1-t, tuple(p))
        ret[0] += a * roll[k]
        ret[1] += b * roll[k]
    return ret

print(dp((21, 21), 0, tuple(p)))