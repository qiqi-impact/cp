from functools import cache
from collections import defaultdict, deque
import math

sm = 0
st = 1
d = defaultdict(int)
with open("in") as f:
    for i, a in enumerate(f.read().splitlines()):
        a = a.split(": ")[1]
        b, c = a.split(' | ')
        b = [int(x) for x in b.split(' ') if x]
        c = [int(x) for x in c.split(' ') if x]
        v = len(set(b) & set(c))
        if i in d:
            st -= d[i]
        cur = st
        d[i+v+1] += cur
        st += cur
        sm += cur
print(sm)
