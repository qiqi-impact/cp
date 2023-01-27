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
        ct = int(c[x-1] == b) + int(c[y-1] == b)
        ret += int(ct == 1)
    print(ret)