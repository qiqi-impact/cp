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
        lines.append(a)

d = 3
cx, cy = None, None
R, C = len(lines), len(lines[0])
for i in range(R):
    for j in range(C):
        if lines[i][j] == '^':
            cx, cy = i, j

while 0 <= cx < R and 0 <= cy < C:
    s.add((cx, cy))
    nx, ny = cx + DIR[d][0], cy + DIR[d][1]
    while 0 <= nx < R and 0 <= ny < C and lines[nx][ny] == '#':
        d = (d+1)%4
        nx, ny = cx + DIR[d][0], cy + DIR[d][1]
    cx, cy = nx, ny

print(len(s))
    