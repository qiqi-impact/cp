from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

ret = 0
s = set()
d = defaultdict(list)
with open("in") as f:
    for x in f.read().splitlines():
        words = x.split(' ')
        k = ' '.join(words[:3])
        rest = ' '.join(words[4:])[:-1]
        l = rest.split(', ')
        for y in l:
            a, b = y.split(' ', 1)
            a = int(a)
            if a == 1:
                b += 's'
            d[a].append()
ret += len(s)
print(ret)