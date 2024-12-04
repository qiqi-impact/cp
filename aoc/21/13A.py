from functools import cache
from collections import defaultdict, deque
import math

g = []
dots = set()

ret = 0
stage = 0
R, C = 0, 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        if len(l) == 0:
            stage = 1

            
            for i in range(R):
                x = []
                for j in range(C):
                    x.append(int((i, j) in dots))
                g.append(x)
            # print(g)

            continue
        if stage == 0:
            a, b = l.split(',')
            dots.add((int(b), int(a)))
            R = max(R, int(b)+1)
            C = max(C, int(a)+1)
        elif stage == 1:
            t = l.split(' ')[-1]
            axis, val = t.split('=')
            val = int(val)

            if axis == 'y':
                for i in range(val+1, R):
                    for j in range(C):
                        g[2 * val - i][j] = max(g[i][j], g[2 * val - i][j])
                R = val
            else:
                for j in range(val+1, C):
                    for i in range(R):
                        g[i][2 * val - j] = max(g[i][j], g[i][2 * val - j])
                C = val
            break

for i in range(R):
    for j in range(C):
        if g[i][j]:
            ret += 1
print(ret)

