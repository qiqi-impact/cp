from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re
import json

ret = 0
with open("in") as f:
    for x in f.read().splitlines():
        x = x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
        v = int(x, 2)
        ret = max(v, ret)
    print(ret)