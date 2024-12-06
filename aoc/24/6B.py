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
s = set()
with open("in") as f:
    for a in f.read().splitlines():
        lines.append([c for c in a])

ret = 0

R, C = len(lines), len(lines[0])
for i in range(R):
    for j in range(C):
        if lines[i][j] == '^':
            scx, scy = i, j

for i in range(R):
    for j in range(C):
        if lines[i][j] == '.':
            print(i, j)
            lines[i][j] = '#'
            s = set()
            d = 3
            cx, cy = scx, scy
            while 0 <= cx < R and 0 <= cy < C:
                if (cx, cy, d) in s:
                    ret += 1
                    break
                s.add((cx, cy, d))
                nx, ny = cx + DIR[d][0], cy + DIR[d][1]
                while 0 <= nx < R and 0 <= ny < C and lines[nx][ny] == '#':
                    d = (d+1)%4
                    nx, ny = cx + DIR[d][0], cy + DIR[d][1]
                cx, cy = nx, ny
            lines[i][j] = '.'

print(ret)
    
