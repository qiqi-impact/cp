from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

lines = [[]]
with open("in") as f:
    for a in f.read().splitlines():
        if not a.strip():
            lines.append([])
        else:
            lines[-1].append(a)

ln = len(lines)
ret = 0

def val(x):
    R, C = len(x), len(x[0])
    rn, cn = -1, -1

    def match_col(j, k):
        if not (0 <= j < C) or not (0 <= k < C):
            return 1
        f = 1
        for i in range(R):
            if x[i][j] != x[i][k]:
                f = 0
        return f

    def match_row(i, k):
        if not (0 <= i < R) or not (0 <= k < R):
            return 1
        f = 1
        for j in range(C):
            if x[i][j] != x[k][j]:
                f = 0
        return f

    s = set()

    for j in range(C-1):
        f = 1
        for df in range(C):
            if not match_col(j-df, j+1+df):
                f = 0
        if f:
            s.add(('c', j+1))

    for i in range(R-1):
        f = 1
        for df in range(R):
            if not match_row(i-df, i+1+df):
                f = 0
                break
        if f:
            s.add(('r', i+1))
    return s

ret = 0
for _, x in enumerate(lines):
    R, C = len(x), len(x[0])
    t, v = list(val(x))[0]
    print(t, v)
    f = 0
    for i in range(R):
        for j in range(C):
            opp = '#' if (x[i][j] == '.') else '.'
            ox = x[i][:]
            x[i] = x[i][:j] + opp + x[i][j+1:]
            qq = val(x)
            x[i] = ox
            # print(i, j, q)
            if qq:
                for q in qq:
                    if (q[0] != t or q[1] != v):
                        ret += 100*q[1] if q[0] == 'r' else q[1]
                        f = 1
                        break
            if f:
                break
        if f:
            break



print(ret)