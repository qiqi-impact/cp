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

for i in range(R):
    for j in range(C):
        if lines[i][j] == 'S':
            lines[i] = lines[i][:j] + '.' + lines[i][j+1:]

@cache
def parity(sx, sy, D):
    dist = {(sx, sy): 0}
    q = deque([(sx, sy)])
    ret = [1, 0]
    while q:
        x, y = q.popleft()
        if dist[x, y] == D:
            continue
        for dx, dy in dirmap.values():
            nx, ny = x+dx, y+dy
            if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] in '.':
                if (nx, ny) not in dist:
                    dist[nx, ny] = 1 + dist[x, y]
                    ret[dist[nx, ny]%2] += 1
                    q.append((nx, ny))
    print(sx, sy, D, ret)
    return ret

N = 26501365 // R
# N = 2
MID = (R-1)//2
ans = 0

x, y = parity(MID, MID, 1000)
ans += N*N*x + (N-1)*(N-1)*y

for a in [0, R-1]:
    for b in [0, C-1]:
        x, y = parity(a, b, MID-1)
        ans += N*x

for (a, b) in [(MID, 0), (MID, R-1), (0, MID), (R-1, MID)]:
    x, y = parity(a, b, R-1)
    ans += x

for a in [0, R-1]:
    for b in [0, C-1]:
        x, y = parity(a, b, R-1+MID)
        ans += (N-1)*y

print(ans)