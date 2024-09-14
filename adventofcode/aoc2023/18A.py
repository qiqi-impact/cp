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
L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

cx, cy = 0, 0
dug = set([(0, 0)])
check = None

for l in lines:
    a,b,c = l.split(' ')
    b = int(b)
    dx, dy = dirmap[a]
    dx *= b
    dy *= b
    if not check:
        if dx:
            check = [(cx+dx//b, cy+1), (cx+dx//b, cy-1)]
        else:
            check = [(cx+1, cy+dy//b), (cx-1, cy+dy//b)]
    if dx > 0:
        for i in range(cx+1, cx+dx+1):
            cx = i
            dug.add((i, cy))
    elif dx < 0:
        for i in range(cx-1, cx+dx-1, -1):
            cx = i
            dug.add((i, cy))
    elif dy > 0:
        for i in range(cy+1, cy+dy+1):
            cy = i
            dug.add((cx, i))
    elif dy < 0:
        for i in range(cy-1, cy+dy-1, -1):
            cy = i
            dug.add((cx, i))
    # print((cx, cy))

bd = len(dug)

# for i in range(10):
#     s = ''
#     for j in range(10):
#         s += '#' if (i, j) in dug else '.'
#     print(s)

    
aq, bq = deque([check[0]]), deque([check[1]])
dug.add((check[0]))
dug.add((check[1]))
ac, bc = 1, 1
while aq and bq:
    x, y = aq.popleft()
    # print(x, y)
    for dx, dy in DIR:
        nx, ny = x+dx, y+dy
        if (nx, ny) not in dug:
            dug.add((nx, ny))
            ac += 1
            aq.append((nx, ny))

    x, y = bq.popleft()
    # print(x, y)
    for dx, dy in DIR:
        nx, ny = x+dx, y+dy
        if (nx, ny) not in dug:
            dug.add((nx, ny))
            bc += 1
            bq.append((nx, ny))

    # print(aq, bq)
    # for i in range(10):
    #     s = ''
    #     for j in range(10):
    #         s += '#' if (i, j) in dug else '.'
    #     print(s)
    # print(len(aq), len(bq))
    # input()

# for i in range(10):
#     s = ''
#     for j in range(10):
#         s += '#' if (i, j) in dug else '.'
#     print(s)


if not aq:
    print(ac + bd)
else:
    print(bc + bd)