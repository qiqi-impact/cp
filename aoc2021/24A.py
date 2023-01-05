from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re, json

def div(l, r):
    if l < 0 and r < 0:
        l = -l
        r = -r
        l //= r
    elif l < 0 or r < 0:
        l = abs(l)
        r = abs(r)
        l //= r
        l = -l
    else:
        l //= r
    return l

def simulate(inst, w, z):
    reg = [w, 0, 0, z]
    for m, l, r in inst:
        l = ord(l) - ord('w')
        if type(r) != int:
            r = reg[ord(r) - ord('w')]
        if m == 'add':
            reg[l] += r
        elif m == 'mod':
            reg[l] = reg[l] - div(reg[l], r) * r
        elif m == 'mul':
            reg[l] *= r
        elif m == 'div':
            reg[l] = div(reg[l], r)
        elif m == 'eql':
            reg[l] = int(reg[l] == r)
    return reg[-1]

groups = []
zopts = set([0])
ret = ''
with open('in') as f:
    for _, l in enumerate(f.read().splitlines()):
        t = l.split(' ')
        if len(t) == 2:
            # if groups:
            #     r = set()
            #     for i in range(9, 0, -1):
            #         for z in zopts:
            #             r.add(simulate(groups[-1], i, z))
            #     zopts = r
            #     print(min(zopts), max(zopts))
            #     input()
            groups.append([])
            continue
        try:
            t[2] = int(t[2])
        except:
            pass
        groups[-1].append(t)

for i in range(11111111111111, 10**14):
    print(i)
    z = 0
    for j, x in enumerate([int(c) for c in str(i)]):
        z = simulate(groups[j], x, z)
        print(z)
        input()
    print(i, z)
    input()

# r = set()
# for i in range(9, 0, -1):
#     for z in zopts:
#         r.add(simulate(groups[-1], i, z))
# zopts = r
# print(0 in zopts)

