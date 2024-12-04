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

cur = 1
for i in range(1, 1000):
    pl = (i-1)%2
    p[pl] += 3 * cur + 3 - 1
    p[pl] %= 10
    p[pl] += 1
    score[pl] += p[pl]
    if score[pl] >= 1000:
        print(score[1-pl] * i * 3)
        break
    cur += 3