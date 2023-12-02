from functools import cache
from collections import defaultdict, deque
import math

with open("in") as f:
    for a in f.read().splitlines():
        try:
            b = int(a)
            break
        except:
            pass