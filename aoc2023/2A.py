from functools import cache
from collections import defaultdict, deque
import math

mx = {'red': 12, 'green':13, 'blue':14}

with open("in") as f:
    ret = 0
    i = 0
    for x in f.read().splitlines():
        fail = 0
        i += 1
        x = x.split(': ')[1]
        l = x.split('; ')
        for t in l:
            q = t.split(', ')
            for y in q:
                v = y.split(' ')
                a, b = int(v[0]), v[1]
                if a > mx[b]:
                    fail = 1
        if not fail:
            ret += i
    print(ret)
