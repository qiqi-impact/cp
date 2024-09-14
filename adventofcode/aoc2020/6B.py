from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

ret = 0
s = set()
ct = 0
with open("in") as f:
    for x in f.read().splitlines():
        print(x, len(x))
        if x.strip() == '':
            ret += len(s)
            print(len(s))
            s = set()
            ct = 0
        else:
            if not ct:
                s |= set(x)
            else:
                s &= set(x)
            ct += 1
    ret += len(s)
    print(ret)