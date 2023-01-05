from functools import cache
from collections import defaultdict, deque, Counter
import itertools
import heapq
import math
import re, json

def simulate(inst, v):
    reg = [v, 0, 0, 0]
    for m, l, r in inst:
        # print(m, l, r)
        l = ord(l) - ord('w')
        if type(r) != int:
            r = reg[ord(r) - ord('w')]
        # print(l, r)
        if m == 'add':
            reg[l] += r
        elif m == 'mod':
            reg[l] %= r
        elif m == 'mul':
            reg[l] *= r
        elif m == 'div':
            if reg[l] < 0 and r < 0:
                reg[l] = -reg[l]
                r = -r
                reg[l] //= r
            elif l < 0 or r < 0:
                reg[l] = abs(reg[l])
                r = abs(r)
                reg[l] //= r
                reg[l] = -l
            else:
                reg[l] //= r
        elif m == 'eql':
            reg[l] = int(reg[l] == r)
        print(reg)
        input()
    return reg[-1] == 0


groups = []
ret = ''
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        t = l.split(' ')
        if len(t) == 2:
            if groups:
                for i in range(9, 0, -1):
                    if simulate(groups[-1], i):
                        ret += str(mx)
                        break
            groups.append([])
            continue
        try:
            t[2] = int(t[2])
        except:
            pass
        groups[-1].append(t)
for i in range(9, 0, -1):
    if simulate(groups[-1], i):
        ret += str(mx)
        break
print(ret)