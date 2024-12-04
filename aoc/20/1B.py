from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

s = set()
d = {}

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        v = int(l)
        if 2020-v in d:
            a, b = d[2020-v]
            print(a*b*v)
        for x in s:
            d[x+v] = (x, v)
        s.add(v)