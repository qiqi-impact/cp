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

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
ln = len(lines)

RR, CC = ln, len(lines[0])
for i in range(RR):
    for j in range(CC):
        if lines[i][j] == 'S':
            sx, sy = i, j

U, D, L, R = [[-1, 0], [1, 0], [0, -1], [0, 1]]


dd = {
    'S': [U, D, L, R],
    '-': [L, R],
    '|': [U, D],
    'L': [U, R],
    'J': [U, L],
    '7': [L, D],
    'F': [D, R],
}


q = deque([(sx, sy)])
ret = 0
dist = [[10**9 for _ in range(CC)] for _ in range(RR)]
dist[sx][sy] = 0
while q:
    cx, cy = q.popleft()
    v = lines[cx][cy]

    if v == 'S':
        t = []
        for dx, dy in [U, D, L, R]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < RR and 0 <= ny < CC:
                vv = lines[nx][ny]
                if (dx, dy) == tuple(U) and vv in '|7F':
                    t.append(U)
                if (dx, dy) == tuple(D) and vv in '|JL':
                    t.append(D)
                if (dx, dy) == tuple(L) and vv in '-LF':
                    t.append(L)
                if (dx, dy) == tuple(R) and vv in '-J7':
                    t.append(R)
    else:
        t = dd[v]

    for dx, dy in t:
        nx, ny = cx+dx, cy+dy
        if 0 <= nx < RR and 0 <= ny < CC and dist[nx][ny] == 10**9 and lines[nx][ny] != '.':
            dist[nx][ny] = dist[cx][cy] + 1
            ret = max(ret, dist[nx][ny])
            q.append((nx, ny))
print(ret)