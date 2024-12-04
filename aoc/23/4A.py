from functools import cache
from collections import defaultdict, deque
import math

ret = 0
with open("in") as f:
    for a in f.read().splitlines():
        a = a.split(": ")[1]
        b, c = a.split(' | ')
        b = [int(x) for x in b.split(' ') if x]
        c = [int(x) for x in c.split(' ') if x]
        v = len(set(b) & set(c))
        if v:
            ret += 1 << (v-1)
print(ret)
    