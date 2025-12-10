from functools import cache
from collections import defaultdict, deque
import math
import bisect

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def grabint(s, idx):
    cur = 0
    ln = 0
    for i in range(idx, len(s)):
        try:
            cur = 10 * cur + int(s[i])
        except:
            return cur, i
    return cur, len(s)

def colon(s):
    return s.split(': ')[1]

def merge(l):
    return ''.join([str(x) for x in l])

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

# dirmap = {
#     'R': [0, 1],
#     'L': [0, -1],
#     'U': [-1, 0],
#     'D': [1, 0],
# }
# L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
# DIR = [R, D, L, U]

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        # lines.append(a)
        lines.append(ints(a, ',')[::-1])

ln = len(lines)

xm = {}
ym = {}
red_set = set()

xs = set()
ys = set()

for x, y in lines:
    xs.add(x)
    ys.add(y)

xl = sorted(list(xs))
yl = sorted(list(ys))
for i in range(len(xl)):
    xm[xl[i]] = i
for i in range(len(yl)):
    ym[yl[i]] = i

norm = [(xm[x], ym[y]) for (x, y) in lines]

R, C = len(xm), len(ym)

grid = [[0 for _ in range(C)] for _ in range(R)]

def prt():
    for i in range(R):
        for j in range(C):
            print('X' if grid[i][j] else '.', end='')
        print()

ret = 0
p, q = None, None

turns = ''
safe_offset = None

rbr = defaultdict(list)
for x, y in norm:
    rbr[x].append(y)

for i in range(ln + 1):
    a, b = norm[i%ln]
    if i != 0:
        if a == p:
            if b < q:
                turns += 'L'
            else:
                turns += 'R'
            for k in range(min(b,q), 1 + max(b,q)):
                grid[a][k] = 1
        else:
            if a < p:
                turns += 'U'
            else:
                turns += 'D'
            for k in range(min(a,p), 1 + max(a,p)):
                grid[k][b] = 1
        if len(turns) == 2:
            if turns == 'LU' or turns == 'DR':
                safe_offset = [-1,1]
            elif turns == 'LD' or turns == 'UR':
                safe_offset = [1,1]
            elif turns == 'RU' or turns == 'DL':
                safe_offset = [-1,-1]
            else:
                safe_offset = [1,-1]
    p, q = a, b

st = (norm[1][0] + safe_offset[0], norm[1][1] + safe_offset[1])
fq = deque([st])
grid[st[0]][st[1]] = 1

bound = {}

while fq:
    x, y = fq.popleft()
    for dx, dy in [[0,-1], [0,1], [-1,0], [1,0]]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0:
            fq.append((nx, ny))
            grid[nx][ny] = 1

dead = set()

# prt()
# input()

for i in range(R):
    iv = []
    st = None
    for j in range(C):
        if grid[i][j] == 1:
            if st is None:
                st = j
        else:
            if st is not None:
                iv.append((st, j-1))
                st = None
    if st is not None:
        iv.append((st, C-1))
    for c in rbr[i]:
        bound[(i,c)] = (0, C-1)
    # print(iv)
    # input()
    for x, y in list(bound.keys()):
        if (x, y) in dead:
            continue
        idx = bisect.bisect_left(iv, (y, 100000)) - 1
        if idx >= 0:
            l, r = iv[idx]
            if y > r:
                # print('dead', x, y)
                dead.add((x, y))
            else:
                bound[x,y] = (max(bound[x,y][0], l), min(bound[x,y][1], r))
        else:
            # print('dead', x, y)
            dead.add((x, y))
    for c in rbr[i]:
        # print(c)
        for x, y in bound:
            if (x, y) in dead:
                continue
            l, r = bound[x, y]
            if l <= c <= r:
                # print('valid', (x, y), (i, c), (abs(xl[x] - xl[i]) + 1), (abs(yl[y] - yl[c]) + 1))
                ret = max(ret, (abs(xl[x] - xl[i]) + 1) * (abs(yl[y] - yl[c]) + 1))
    # print(i, bound)
print(ret)