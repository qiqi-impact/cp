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
        lines.append([c for c in a])
ln = len(lines)

U, D, L, R = [[-1, 0], [1, 0], [0, -1], [0, 1]]

dd = {
    '-': [L, R],
    '|': [U, D],
    'L': [U, R],
    'J': [U, L],
    '7': [L, D],
    'F': [D, R],
}

RR, CC = ln, len(lines[0])
t = []
for i in range(RR):
    for j in range(CC):
        if lines[i][j] == 'S':
            sx, sy = i, j

            
            for dx, dy in [U, D, L, R]:
                nx, ny = i+dx, j+dy
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
            
            t.sort()
            for k in dd:
                if sorted(dd[k]) == t:
                    lines[i][j] = k

cx, cy = sx, sy
nx, ny = cx+t[0][0], cy+t[0][1]
s = set([(sx, sy), (nx, ny)])
# print(sx, sy)
area = 0
while 1:
    # print(nx, ny)
    area += (cx - nx) * (cy + ny)
    cx, cy = nx, ny
    v = lines[cx][cy]
    f = 0
    for t in dd[v]:
        nx, ny = cx+t[0], cy+t[1]
        if (nx, ny) not in s:
            s.add((nx, ny))
            f = 1
            break
    if not f:
        break
area += (cx - sx) * (cy + sy)
print(abs(area)//2 - len(s)//2 + 1)