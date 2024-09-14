from functools import cache
from collections import defaultdict, deque
import math

d = defaultdict(int)

ret = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        a, b = l.split(' | ')
        for x in b.split(' '):
            if len(x) in [2,3,4,7]:
                ret += 1
print(ret)