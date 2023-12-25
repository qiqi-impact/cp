from functools import cache
from collections import defaultdict, deque
import math
import sys

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

def opts(i, j):
    v = lines[i][j]
    if v == '<':
        return [[0,-1]]
    elif v == '>':
        return [[0,1]]
    elif v == '^':
        return [[-1,0]]
    elif v == 'v':
        return [[1,0]]
    return [[0,-1], [0,1], [-1,0], [1,0]]

seen = set([(0, 1)])
ret = 0
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
dfs(0, 1)
print(ret-1)