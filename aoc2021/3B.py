from functools import cache
from collections import defaultdict, deque
import math

N = 12

ret = 0
ll = [0] * N
ct = 0
s = set()
t = set()
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        for j, c in enumerate(l):
            ll[j] += int(c)
        s.add(l)
        ct += 1
t = s.copy()

g, e = 0, 0
ss = tt = None
for j in range(N):
    g *= 2
    e *= 2

    sc, tc = .5, .5
    for x in s:
        sc += 1 if x[j] == '1' else -1
    for x in t:
        tc += 1 if x[j] == '1' else -1

    if sc > 0:
        s = {x for x in s if x[j] == '1'}
    else:
        s = {x for x in s if x[j] == '0'}

    if tc > 0:
        t = {x for x in t if x[j] == '0'}
    else:
        t = {x for x in t if x[j] == '1'}

    if len(s) == 1:
        ss = s.pop()
    if len(t) == 1:
        tt = t.pop()

# print(ss, tt)

a, b = 0, 0
for j in range(N):
    a *= 2
    b *= 2
    a += int(ss[j])
    b += int(tt[j])
print(a * b)