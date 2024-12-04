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

dirmap = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0],
}

R, C = ln, len(lines[0])

dist = {}
q = deque()

for i in range(R):
    for j in range(C):
        if lines[i][j] == 'S':
            q.append((i, j))
            dist[i, j] = 0

while q:
    x, y = q.popleft()
    if dist[x, y] == 64:
        continue
    for dx, dy in dirmap.values():
        nx, ny = x+dx, y+dy
        if lines[nx%R][ny%C] in 'S.':
            if (nx, ny) not in dist:
                dist[nx, ny] = 1 + dist[x, y]
                q.append((nx, ny))

ret = 0
for v in dist.values():
    if v%2 == 0:
        ret += 1
print(ret)