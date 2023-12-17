from functools import cache
from collections import defaultdict, deque
import math
import heapq

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

inf = 10**18

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
ln = len(lines)


R, C = ln, len(lines[0])
grid = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        grid[i][j] = int(lines[i][j])



L, Q, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [Q, D, L, U]

START = 0, (0, 0, 0)
START2 = 0, (0, 0, 1)
END = (R-1, C-1)
h = [START, START2]
dist = {START[1]: 0, START2[1]: 0}
while h:
    cost, cur = heapq.heappop(h)
    # print(cost, cur)
    if dist[cur] != cost:
        continue
    if (cur[0], cur[1]) == END:
        print(cost)
        break

    if cur[2] in [0, 2]:
        OPTS = [1, 3]
    else:
        OPTS = [0, 2]

    for idx in OPTS:
        nc = cost
        for L in range(1, 11):
            nx, ny = cur[0]+L*DIR[idx][0], cur[1]+L*DIR[idx][1]
            if 0 <= nx < R and 0 <= ny < C:
                nc += grid[nx][ny]
                if L >= 4 and dist.get((nx, ny, idx), inf) > nc:
                    dist[nx, ny, idx] = nc
                    heapq.heappush(h, (nc, (nx, ny, idx)))