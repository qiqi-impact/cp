from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

s = set()
with open("in") as f:
    for x in f.read().splitlines():
        x = x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        v = int(x, 2)
        s.add(v)
for i in range(1000000):
    if i-1 in s and i+1 in s and i not in s:
        print(i)
        break