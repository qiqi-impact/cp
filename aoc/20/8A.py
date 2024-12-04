from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

acc = 0
l = []
with open("in") as f:
    for a in f.read().splitlines():
        x, y = a.split(' ')
        y = int(y)
        if x == 'nop':
            x = 'jmp'
            y = 1
        l.append((x, y))
s = set()
cur = 0
while cur not in s:
    s.add(cur)
    x, y = l[cur]
    if x == 'acc':
        acc += y
        cur += 1
    else:
        cur += y
print(acc)