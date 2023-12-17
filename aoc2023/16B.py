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

X, Y = ln, len(lines[0])

L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

def f(p):
    q = deque([p])
    s = set()
    ss = set()
    while q:
        x, y, d = q.popleft()
        # print(x, y, d)
        s.add((x, y, d))
        ss.add((x, y))
        v = lines[x][y]
        if v == '.':
            nx, ny = x+DIR[d][0], y+DIR[d][1]
            if 0 <= nx < X and 0 <= ny < Y and (nx, ny, d) not in s:
                q.append((nx, ny, d))
        elif v == '|':
            if d in [3, 1]:
                nx, ny = x+DIR[d][0], y+DIR[d][1]
                if 0 <= nx < X and 0 <= ny < Y and (nx, ny, d) not in s:
                    q.append((nx, ny, d))
            else:
                for d in [1, 3]:
                    nx, ny = x+DIR[d][0], y+DIR[d][1]
                    if 0 <= nx < X and 0 <= ny < Y and (nx, ny, d) not in s:
                        q.append((nx, ny, d))
        elif v == '-':
            if d in [0, 2]:
                nx, ny = x+DIR[d][0], y+DIR[d][1]
                if 0 <= nx < X and 0 <= ny < Y and (nx, ny, d) not in s:
                    q.append((nx, ny, d))
            else:
                for d in [0, 2]:
                    nx, ny = x+DIR[d][0], y+DIR[d][1]
                    if 0 <= nx < X and 0 <= ny < Y and (nx, ny, d) not in s:
                        q.append((nx, ny, d))
        elif v == '/':
            if d == 2: d = 1
            elif d == 1: d = 2
            elif d == 0: d = 3
            elif d == 3: d = 0
            nx, ny = x+DIR[d][0], y+DIR[d][1]
            if 0 <= nx < X and 0 <= ny < Y and (nx, ny, d) not in s:
                q.append((nx, ny, d))
        elif v == '\\':
            if d == 2: d = 3
            elif d == 3: d = 2
            elif d == 1: d = 0
            elif d == 0: d = 1
            nx, ny = x+DIR[d][0], y+DIR[d][1]
            if 0 <= nx < X and 0 <= ny < Y and (nx, ny, d) not in s:
                q.append((nx, ny, d))
    return len(ss)

ret = 0
for i in range(X):
    ret = max(ret, f((i, 0, 0)))
    ret = max(ret, f((i, Y-1, 2)))
for j in range(Y):
    ret = max(ret, f((0, j, 1)))
    ret = max(ret, f((X-1, j, 1)))
print(ret)