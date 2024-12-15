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

step = 0
lines = []
moves = ''
with open("in") as f:
    for a in f.read().splitlines():
        if step == 0:
            if a == '':
                step = 1
                continue
            lines.append([c for c in a])
        elif step == 1:
            moves += a



RR, CC = len(lines), len(lines[0])
cx, cy = None, None
for i in range(RR):
    for j in range(CC):
        if lines[i][j] == '@':
            cx, cy = i, j

dd = {
    '>': R,
    '<': L,
    '^': U,
    'v': D,
}

def blocked(i, j, dx, dy):
    if lines[i][j] == '#':
        return True
    if lines[i][j] == '.':
        return False
    return blocked(i+dx, j+dy, dx, dy)

def push(c, i, j, dx, dy):
    if lines[i][j] == '.':
        lines[i][j] = c
    elif lines[i][j] == 'O':
        lines[i][j] = c
        push('O', i+dx, j+dy, dx, dy)

print(moves)
for c in moves:
    dx, dy = dd[c]
    # print(dx, dy)
    nx, ny = cx + dx, cy + dy
    if not blocked(nx, ny, dx, dy):
        lines[cx][cy] = '.'
        cx, cy = nx, ny
        push('@', cx, cy, dx, dy)
        # print(cx, cy)

# for l in lines:
#     print(''.join(l))

ret = 0
for i in range(RR):
    for j in range(CC):
        if lines[i][j] == 'O':
            ret += 100 * i + j
print(ret)