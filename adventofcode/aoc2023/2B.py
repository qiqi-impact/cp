from functools import cache
from collections import defaultdict, deque
import math

mx = {'red': 12, 'green':13, 'blue':14}

with open("in") as f:
    ret = 0
    i = 0
    for x in f.read().splitlines():
        i += 1
        x = x.split(': ')[1]
        l = x.split('; ')
        Y = {'red':0, 'green':0, 'blue':0}
        for t in l:
            q = t.split(', ')
            for y in q:
                v = y.split(' ')
                a, b = int(v[0]), v[1]
                Y[b] = max(Y[b], a)
        l = list(Y.values())
        ret += l[0]* l[1] * l[2]
    print(ret)
