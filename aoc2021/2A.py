from functools import cache
from collections import defaultdict, deque
import math

ret = 0
x, y = 0, 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        op, v = l.split(' ')
        v = int(v)
        if op[0] == 'f':
            y += v
        elif op[0] == 'u':
            x -= v
        else:
            x += v

print(x*y)