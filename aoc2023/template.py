from functools import cache
from collections import defaultdict, deque
import math

with open("in") as f:
    for x in f.read().splitlines():
        try:
            c = int(x)
            break
        except:
            pass