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

bricks = []
for t, l in enumerate(lines):
    p = l.split('~')
    br = []
    for a in p:
        br.append(ints(a, ','))
    for i in range(3):
        if br[0][i] != br[1][i]:
            br.append(i)
            br[0][i], br[1][i] = min(br[0][i], br[1][i]), max(br[0][i], br[1][i])
    if len(br) == 2:
        br.append(-1)
    br.append(t)
    bricks.append(br)

g = defaultdict(list)
ind = defaultdict(int)

bricks.sort(key=lambda x:x[0][2])

settled = []

for b in bricks:
    while b[0][2] > 1:
        mz = b[0][2]
        w, x, y, z = b[0][0], b[1][0], b[0][1], b[1][1]

        f = 0
        for s in settled:
            if s[1][2] == mz-1:
                area = set()
                for i in range(s[0][0], s[1][0]+1):
                    for j in range(s[0][1], s[1][1]+1):
                        area.add((i, j))
                r = 0
                for i in range(w, x+1):
                    for j in range(y, z+1):
                        if (i, j) in area:
                            f = 1
                            r = 1
                            g[s[3]].append(b[3])
                            ind[b[3]] += 1
                            break
                    if r: break
        if f: break
        b[0][2] -= 1
        b[1][2] -= 1
    settled.append(b)

# print(g)
# print(ind)

ret = 0
for k in range(ln):
    f = 1
    for x in g[k]:
        if ind[x] == 1:
            f = 0
            break
    ret += f
    # if f: print(k)
print(ret)