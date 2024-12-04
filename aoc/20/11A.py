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

# dirmap = {
#     'R': [0, 1],
#     'L': [0, -1],
#     'U': [-1, 0],
#     'D': [1, 0],
# }
L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append([c for c in a])
R, C = len(lines), len(lines[0])

ch = True
while ch:
    ch = False
    for i in range(R):
        for j in range(C):
            if lines[i][j] == 'L':
                occ = False
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx != 0 or dy != 0:
                            nx, ny = i+dx, j+dy
                            if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] in ['#', '<']:
                                occ = True
                if not occ:
                    ch = True
                    lines[i][j] = '>'
            elif lines[i][j] == '#':
                occ = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx != 0 or dy != 0:
                            nx, ny = i+dx, j+dy
                            if 0 <= nx < R and 0 <= ny < C and lines[nx][ny] in ['#', '<']:
                                occ += 1
                if occ >= 4:
                    ch = True
                    lines[i][j] = '<'
    for i in range(R):
        for j in range(C):
            if lines[i][j] == '>':
                lines[i][j] = '#'
            elif lines[i][j] == '<':
                lines[i][j] = 'L'
ret = 0
for l in lines:
    ret += l.count('#')
print(ret)