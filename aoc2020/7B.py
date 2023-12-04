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
def amt(k):
    ret = 1
    for x, y in d[k]:
        ret += amt(x) * y
    # print(k, ret)
    return ret

print(amt('shiny gold bags')-1)
