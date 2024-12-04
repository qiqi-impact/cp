from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re

ev = {}
oo = []

with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        ll = re.split(' |=|\.\.|,', l)
        oo.append(ll[0] == 'on')

        t = []
        for x in ll:
            try:
                t.append(int(x))
            except:
                pass

        a, b, c, d, e, f = t
        b += 1
        d += 1
        f += 1
        if a not in ev: ev[a] = {}
        if b not in ev: ev[b] = {}

        if c not in ev[a]: ev[a][c] = {}
        if d not in ev[a]: ev[a][d] = {}
        if c not in ev[b]: ev[b][c] = {}

        if e not in ev[a][c]: ev[a][c][e] = [set(), set()]
        if f not in ev[a][c]: ev[a][c][f] = [set(), set()]
        if e not in ev[a][d]: ev[a][d][e] = [set(), set()]
        if e not in ev[b][c]: ev[b][c][e] = [set(), set()]
        
        ev[a][c][e][0].add(i)
        ev[a][c][f][1].add(i)
        ev[a][d][e][1].add(i)
        ev[b][c][e][1].add(i)

    oo.append(False)

    xev = {}
    lx = None
    ret = 0
    step = 1
    for x in sorted(ev.keys()):
        print(step)
        step += 1
        if lx is not None:
            ret += (x - lx) * area
        for y in ev[x]:
            if y not in xev: xev[y] = {}
            for z in ev[x][y]:
                if z not in xev[y]:
                    xev[y][z] = [set(), set()]
                xev[y][z][0] |= ev[x][y][z][0]
                xev[y][z][1] |= ev[x][y][z][1]
        cev = {}
        ly = None
        area = 0
        for y in sorted(xev.keys()):
            if ly is not None:
                area += (y - ly) * ln
            for z in xev[y]:
                if z not in cev: cev[z] = [set(), set()]
                cev[z][0] |= xev[y][z][0]
                cev[z][1] |= xev[y][z][1]
            st = set()
            op = None
            ln = 0
            for z in sorted(cev.keys()):
                st |= cev[z][0]
                st -= cev[z][1]
                if st:
                    cur = max(st)
                else:
                    cur = -1
                if op is None and oo[cur]:
                    op = z
                elif op is not None and not oo[cur]:
                    ln += z - op
                    op = None
            ly = y
        lx = x
    print(ret)