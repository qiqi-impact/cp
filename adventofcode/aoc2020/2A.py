from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

s = set()

ret = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        a, b, c = l.split(' ')
        x, y = a.split('-')
        x = int(x)
        y = int(y)
        b = b[0]
        f = defaultdict(int)
        for d in c:
            f[d] += 1
        ret += int(x <= f[b] <= y)
    print(ret)