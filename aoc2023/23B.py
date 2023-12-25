from functools import cache
from collections import defaultdict, deque
import math
import sys
from itertools import pairwise

sys.setrecursionlimit(10000)

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

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
ln = len(lines)
R, C = ln, len(lines[0])
lines = [[c for c in r] for r in lines]

def opts(i, j):
    return [[0,-1], [0,1], [-1,0], [1,0]]

def dfs(x, y):
    global R, C, ret
    if x == R-1 and y == C-2:
        ret = max(ret, len(seen))
        return
    for dx, dy in opts(x, y):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] != '#' and (nx, ny) not in seen:
            seen.add((nx, ny))
            dfs(nx, ny)
            seen.discard((nx, ny))

seen2 = set()
ff = 0
chokeidx = [(0, 1)]
def spread(x, y):
    global R, C, ff
    if ff and (x, y) in choke:
        chokeidx.append((x, y))
        ff += 1
    if x == R-1 and y == C-2:
        return True
    for dx, dy in opts(x, y):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] != '#' and (nx, ny) not in seen2:
            seen2.add((nx, ny))
            if spread(nx, ny):
                return True
    return False

choke = set()
for i in range(1, R-1):
    print(i)
    for j in range(1, C-1):
        ret = -1
        seen2 = set([(0, 1)])
        if lines[i][j] == '.':
            lines[i][j] = '#'
            if not spread(0, 1):
                choke.add((i, j))
            lines[i][j] = '.'
ff = 1
# print(choke)

seen2 = set([(0, 1)])
spread(0, 1)
chokeidx.append((R-1, C-2))

def lgt(x, y, fx, fy, r):
    global R, C
    if x == fx and y == fy:
        r[0] = max(r[0], len(seen)-1)
        return
    for dx, dy in opts(x, y):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] != '#' and (nx, ny) not in seen:
            seen.add((nx, ny))
            lgt(nx, ny, fx, fy, r)
            seen.discard((nx, ny))

ret = 0
for a, b in pairwise(chokeidx):
    print(a, b)
    seen = set([(a[0], a[1])])
    rr = [0]
    lgt(*a, *b, rr)
    print(rr[0])
    ret += rr[0]
print(ret)
