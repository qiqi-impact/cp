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

p = []

q = deque([(sx, sy)])
ret = 0
dist = [[10**9 for _ in range(CC)] for _ in range(RR)]
dist[sx][sy] = 0
tot = 1
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
        p = t[:]
    else:
        t = dd[v]

    for dx, dy in t:
        nx, ny = cx+dx, cy+dy
        if 0 <= nx < RR and 0 <= ny < CC and dist[nx][ny] == 10**9 and lines[nx][ny] != '.':
            dist[nx][ny] = dist[cx][cy] + 1
            tot += 1
            ret = max(ret, dist[nx][ny])
            q.append((nx, ny))

# for i in range(RR):
#     s = ''
#     for j in range(CC):
#         s += ('X' if dist[i][j] == 10**9 else '.')
#     print(s)

X, Y = 3*RR, 3*CC
dd['S'] = p
# print(p)

ng = [[[] for _ in range(Y)] for _ in range(X)]
for i in range(RR):
    for j in range(CC):
        v = lines[i][j]
        if dist[i][j] != 10**9:
            for x in [L, R, U, D]:
                if x in dd[v]:
                    ng[3*i+1][3*j+1].append(x)
                    ng[3*i+1+x[0]][3*j+1+x[1]].append([-x[0], -x[1]])

ret = RR * CC - tot

seen = [[0 for _ in range(Y)] for _ in range(X)]

def dfs(i, j):
    ret = 0
    q = deque([(i, j)])
    seen[i][j] = 1
    while q:
        cx, cy = q.popleft()
        for dx, dy in [U, D, L, R]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < X and 0 <= ny < Y and seen[nx][ny] == 0 and not ng[nx][ny]:
                q.append((nx, ny))
                ret += int(nx%3==1) * int(ny%3==1)
                seen[nx][ny] = 1
    return ret

for i in range(X):
    for j in range(Y):
        if (i == 0 or i == X-1) and (j == 0 or j == Y-1) and not seen[i][j]:
            v = dfs(i, j)
            if v >= 0:
                ret -= v
                print(i, j, v)
print(ret)


# print(ret)