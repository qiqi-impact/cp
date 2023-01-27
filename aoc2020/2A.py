from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

s = set()

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        v = int(l)
        if 2020-v in s:
            print(v*(2020-v))
        else:
            s.add(v)