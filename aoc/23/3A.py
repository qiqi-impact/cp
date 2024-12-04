from functools import cache
from collections import defaultdict, deque
import math

with open("in") as f:
    l = []
    for a in f.read().splitlines():
        l.append(a)
    print(l)
    R, C = len(l), len(l[0])
    print(R, C)
    safe = set()
    for i in range(R):
        for j in range(C):
            c = l[i][j]
            if not ('0' <= c <= '9') and c != '.':
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        safe.add((i+dx, j+dy))
    # print(safe)
    ret = 0
    for i in range(R):
        q = 0
        en = False
        sf = False
        for j in range(C):
            try:
                v = int(l[i][j])
                q = 10*q+v
                if (i, j) in safe:
                    sf = True
            except:
                en = True
            if en:
                if sf:
                    ret += q
                q = 0
                sf = False
                en = False
        if sf:
            ret += q
        sf = False
        en = False
    print(ret)