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
R, C = ln, len(lines[0])

grid = [[c for c in r] for r in lines]

def spin(g):
    ng = [['.' for _ in range(C)] for _ in range(R)]

    for j in range(C):
        q = 0
        for i in range(R):
            v = g[i][j]
            if v == '#':
                ng[i][j] = '#'
                q = i+1
            elif v == 'O':
                ng[q][j] = 'O'
                q += 1

    # for r in ng:
    #     print(''.join(r))


    g = ng
    ng = [['.' for _ in range(C)] for _ in range(R)]

    for i in range(R):
        q = 0
        for j in range(C):
            v = g[i][j]
            if v == '#':
                ng[i][j] = '#'
                q = j+1
            elif v == 'O':
                ng[i][q] = 'O'
                q += 1

    # for r in ng:
    #     print(''.join(r))

    g = ng
    ng = [['.' for _ in range(C)] for _ in range(R)]
    

    for j in range(C):
        q = R-1
        for i in range(R-1, -1, -1):
            v = g[i][j]
            if v == '#':
                ng[i][j] = '#'
                q = i-1
            elif v == 'O':
                ng[q][j] = 'O'
                q -= 1
    g = ng
    ng = [['.' for _ in range(C)] for _ in range(R)]

    for i in range(R):
        q = C-1
        for j in range(C-1, -1, -1):
            v = g[i][j]
            if v == '#':
                ng[i][j] = '#'
                q = j-1
            elif v == 'O':
                ng[i][q] = 'O'
                q -= 1

    return ng

# print(grid)

seen = {}
val = {}
os = None

tot = 0
for j in range(C):
    q = R
    for i in range(R):
        v = grid[i][j]
        if v == '#':
            q = R-i-1
        elif v == 'O':
            tot += q
            q -= 1
print(0, tot)

for t in range(1, 1000000001):
    grid = spin(grid)
    # for r in grid:
    #     print(''.join(r))
    # print()
    s = ''

    # tot = 0
    # for j in range(C):
    #     q = R-1
    #     for i in range(R):
    #         v = grid[i][j]
    #         if v == '#':
    #             q = R-i-1
    #         elif v == 'O':
    #             tot += q
    #             q -= 1
    tot = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                tot += R-i
    print(t, tot)
    val[t] = tot

    for r in grid:
        s += ''.join(r)
    if s not in seen:
        seen[s] = t
        
    else:
        per = t - seen[s]
        print(per, t-per+(1000000000 - t)%per)
        break
print(val[t-per+(1000000000 - t)%per])