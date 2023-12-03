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

    gears = defaultdict(list)


    # print(safe)
    ret = 0
    for i in range(R):
        q = 0
        en = False
        grs = set()
        for j in range(C):
            try:
                v = int(l[i][j])
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if 0 <= i+dx < R and 0 <= j+dy < C and l[i+dx][j+dy] == '*':
                            grs.add(((i+dx), (j+dy)))
                q = 10*q+v
            except:
                en = True
            if en:
                ret += q
                for k in grs:
                    gears[k].append(q)
                q = 0
                en = False
                grs = set()
        ret += q
        for k in grs:
            gears[k].append(q)
        sf = False
        en = False

    ans = 0
    for k in gears:
        if len(gears[k]) == 2:
            ans += gears[k][0] * gears[k][1]
    print(ans)