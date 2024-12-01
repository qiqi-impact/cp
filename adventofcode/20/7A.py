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
            if y == 'no other bags':
                continue
            a, b = y.split(' ', 1)
            a = int(a)
            if a == 1:
                b += 's'
            d[k].append((b, a))

@cache
def has(k):
    ret = 0
    for x, _ in d[k]:
        if x == 'shiny gold bags' or has(x):
            ret = 1
    return ret

print(sum([has(k) for k in list(d.keys())]))
