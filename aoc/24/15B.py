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
q = {
    '@': '@.',
    '#': '##',
    'O': '[]',
    '.': '..',
}
with open("in") as f:
    for a in f.read().splitlines():
        if step == 0:
            if a == '':
                step = 1
                continue
            lines.append([r for r in ''.join([q[c] for c in a])])
        elif step == 1:
            moves += a

print(lines)

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

affect = set()

def blocked(i, j, dx, dy):
    if ((i, j)) in affect:
        return
    if lines[i][j] == '#':
        return True
    if lines[i][j] == '.':
        return False
    affect.add((i, j))
    if lines[i][j] == '[':
        if dx:
            return blocked(i, j+1, dx, dy) or blocked(i+dx, j+dy, dx, dy) or blocked(i+dx, j+1+dy, dx, dy)
        else:
            return blocked(i+dx, j+dy, dx, dy)
    if lines[i][j] == ']':
        if dx:
            return blocked(i, j-1, dx, dy) or blocked(i+dx, j+dy, dx, dy) or blocked(i+dx, j-1+dy, dx, dy)
        else:
            return blocked(i+dx, j+dy, dx, dy)

# def push(pc, c, i, j, dx, dy):
#     print(pc, c, i, j, dx, dy)
#     if pc:
#         lines[i-dx][j-dy] = pc
#     if lines[i][j] == '.':
#         lines[i][j] = c
#     elif lines[i][j] == '[':
#         lines[i][j] = c
#         if dx:
#             push(c, '[', i+dx, j+dy, dx, dy)
#             push(None, ']', i+dx, j+1+dy, dx, dy)
#         else:
#             push(c, '[', i+dx, j+dy, dx, dy)
#     else:
#         lines[i][j] = c
#         if dx:
#             push(None, '[', i+dx, j+dy, dx, dy)
#             push(c, ']', i+dx, j-1+dy, dx, dy)
#         else:
#             push(c, ']', i+dx, j+dy, dx, dy)

# print(moves)
# for l in lines:
#     print(''.join(l))
# input()
for c in moves:
    dx, dy = dd[c]
    nx, ny = cx + dx, cy + dy
    affect.clear()

    # if dx:
    #     if lines[nx][ny] == ']':
    #         b = blocked(nx, ny, dx, dy) or blocked(nx, ny-1, dx, dy)
    #     elif lines[nx][ny] == '[':
    #         b = blocked(nx, ny, dx, dy) or blocked(nx, ny+1, dx, dy)
    # else:
    b = blocked(nx, ny, dx, dy)

    if not b:
        affect.add((cx, cy))
        # lines[cx][cy] = '.'
        cx, cy = nx, ny
        # push('.', '@', cx, cy, dx, dy)

        aff = list(affect)
        if dx == 1:
            aff.sort(key=lambda x: -x[0])
        elif dx == -1:
            aff.sort(key=lambda x: x[0])
        elif dy == 1:
            aff.sort(key=lambda x: -x[1])
        elif dy == -1:
            aff.sort(key=lambda x: x[1])

        # print(aff)
        
        for x, y in aff:
            lines[x+dx][y+dy] = lines[x][y]
            lines[x][y] = '.'

        # print(cx, cy)
    # print(c)
for l in lines:
    print(''.join(l))
# input()

ret = 0
for i in range(RR):
    for j in range(CC):
        if lines[i][j] == '[':
            ret += 100 * i + j
print(ret)