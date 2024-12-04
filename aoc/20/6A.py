from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

ret = 0
s = set()
with open("in") as f:
    for x in f.read().splitlines():
        if x.strip() == '':
            ret += len(s)
            s = set()
        else:
            for c in x:
                s.add(c)
ret += len(s)
print(ret)