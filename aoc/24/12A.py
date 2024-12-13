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

def bfs(i, j, c):
    seen = set([(i, j)])
    q = deque([(i, j)])
    p = 0
    while q:
        x, y = q.popleft()
        for dx, dy in DIR:
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C:
                if lines[nx][ny] != c:
                    p += 1
                elif (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny))
            else:
                p += 1
    for x, y in seen:
        lines[x][y] = '.'
    return p * len(seen)

ret = 0
for i in range(R):
    for j in range(C):
        if lines[i][j] != '.':
            ret += bfs(i, j, lines[i][j])
print(ret)