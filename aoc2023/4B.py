from functools import cache
from collections import defaultdict, deque
import math

ret = []
with open("in") as f:
    for a in f.read().splitlines():
        a = a.split(": ")[1]
        b, c = a.split(' | ')
        b = [int(x) for x in b.split(' ') if x]
        c = [int(x) for x in c.split(' ') if x]
        v = len(set(b) & set(c))
        ret.append(v)
ct = [1] * len(ret)
for i in range(len(ret)):
    v = ret[i]
    if v:
        for j in range(i+1, min(i+v+1, len(ret))):
            ct[j] += ct[i]
print(sum(ct))
