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

dist = defaultdict(dict)
def dfs(x, y, sx, sy, fx, fy, r):
    global R, C, dist
    if x == fx and y == fy:
        dist[sx, sy][fx, fy] = r
    for dx, dy in opts(x, y):
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] not in '#F' and (nx, ny) not in seen:
            seen.add((nx, ny))
            dfs(nx, ny, sx, sy, fx, fy, 1+r)
            seen.discard((nx, ny))

viable = set([(0, 1), (R-1, C-2)])

for i in range(1, R-1):
    for j in range(1, C-1):
        ct = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if abs(dx)+abs(dy) == 1 and lines[i+dx][j+dy] in '<>^v':
                    ct += 1
        if ct >= 3:
            lines[i][j] = 'F'
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if lines[i+dx][j+dy] in '<>^v':
                        viable.add((i+dx, j+dy))
                        dist[i, j][i+dx, j+dy] = 1
                        dist[i+dx, j+dy][i, j] = 1

for x, y in viable:
    seen = set([(x, y)])
    for fx, fy in viable:
        if fx != x or fy != y:
            dfs(x, y, x, y, fx, fy, 0)
# print(dist[5, 3])

print(len(viable))

seen = set([(0, 1)])
pp = [(0, 1)]
ret = 0
def dfs2(x, y, tot):
    # print(x, y, tot)
    global R, C, ret
    if x == R-1 and y == C-2:
        if tot > ret:
            ret = tot
            print(x, y, tot, pp)
        return
    for nx, ny in dist[x, y]:
        if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] != '#' and (nx, ny) not in seen:
            seen.add((nx, ny))
            pp.append((nx, ny))
            # if (nx, ny) == (6, 3):
            #     print(dist[x,y][nx,ny])
            dfs2(nx, ny, tot + dist[x, y][nx, ny])
            pp.pop()
            seen.discard((nx, ny))

dfs2(0, 1, 0)
print(ret)