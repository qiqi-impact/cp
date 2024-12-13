from functools import cache
from collections import defaultdict, deque
import math

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

dirmap = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0],
}
L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append([c for c in a])

R, C = len(lines), len(lines[0])

def check_fence(nf, fences):
    x, y, k = nf
    r = 1
    if k in [0, 2]:
        if (x-1, y, k) in fences:
            r -= 1
        if (x+1, y, k) in fences:
            r -= 1
    else:
        if (x, y-1, k) in fences:
            r -= 1
        if (x, y+1, k) in fences:
            r -= 1
    return r

def bfs(i, j, c):
    seen = set([(i, j)])
    fences = set()
    q = deque([(i, j)])
    p = 0
    while q:
        x, y = q.popleft()
        for k, (dx, dy) in enumerate(DIR):
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C:
                if lines[nx][ny] != c:
                    nf = (x, y, k)
                    p += check_fence(nf, fences)
                    fences.add(nf)
                elif (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny))
            else:
                nf = (x, y, k)
                p += check_fence(nf, fences)
                fences.add(nf)
    for x, y in seen:
        lines[x][y] = '.'
    return p * len(seen)

ret = 0
for i in range(R):
    for j in range(C):
        if lines[i][j] != '.':
            ret += bfs(i, j, lines[i][j])
print(ret)