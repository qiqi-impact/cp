from functools import cache
from collections import defaultdict, deque
import math

ret = 0
cur = 1e9
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        x = int(l)
        if x > cur:
            ret += 1
        cur = x
print(ret)