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
            groups.append([])
            continue
        try:
            t[2] = int(t[2])
        except:
            pass
        groups[-1].append(t)

path = []
def dfs(idx, z):
    if idx == 14:
        if z == 0:
            return True
    inst = groups[idx]
    if inst[3][2] == 26:
        v = z%26 + inst[4][2]
        if 1 <= v <= 9:
            path.append(v)
            if dfs(idx+1, simulate(inst, v, z)):
                return True
            path.pop()
    else:
        for v in range(9, 0, -1):
            path.append(v)
            if dfs(idx+1, simulate(inst, v, z)):
                return True
            path.pop()
    return False

dfs(0, 0)
print(''.join(str(x) for x in path))