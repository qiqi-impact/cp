from functools import cache
from collections import defaultdict, deque
import math

s = []

with open('in') as f:
    for line in f.read().splitlines():
        if line.startswith('---'):
            s.append(set())
        elif not line.strip():
            continue
        else:
            a, b, c = [int(x) for x in line.split(',')]
            s[-1].add((a, b, c))

n = len(s)

ss = set([(1,2,3)])
q = [(1, 2, 3)]
qq = []
for a, b, c in q:
    for t in [(a, -c, b), (a, -b, -c), (a, c, -b)]:
        if t not in ss:
            qq.append(t)
            ss.add(t)
q += qq
qq = []
for a, b, c in q:
    for t in [(-c, b, a), (-a, b, -c), (c, b, -a)]:
        if t not in ss:
            qq.append(t)
            ss.add(t)
q += qq
qq = []
for a, b, c in q:
    for t in [(-b, a, c), (-a, -b, c), (b, -a, c)]:
        if t not in ss:
            qq.append(t)
            ss.add(t)
q += qq

rot = [s]
for i in range(1, len(q)):
    nx = []
    for ss in s:
        p = set()
        for x, y, z in ss:
            d = {
                1: x, -1: -x, 2: y, -2: -y, 3: z, -3: -z
            }
            p.add(tuple(d[q[i][t]] for t in range(3)))
        nx.append(p)
    rot.append(nx)

fix = [None] * n
fix[0] = 0
loc = [None] * n
loc[0] = [0, 0, 0]

q = deque([0])
while q:
    i = q.pop()
    print(i)
    for j in range(n):
        found = False
        if fix[j] is None:
            si = rot[fix[i]][i]
            for rj in range(len(rot)):
                sj = rot[rj][j]
                for a in si:
                    for b in sj:
                        df = [b[x]-a[x] for x in range(3)]
                        ct = 0
                        for c in si:
                            cdf = [c[x]+df[x] for x in range(3)]
                            if tuple(cdf) in sj:
                                ct += 1
                        if ct == 12:
                            found = True
                            fix[j] = rj
                            loc[j] = [loc[i][x]-df[x] for x in range(3)]
                            q.append(j)
                            break
                    if found: break
                if found: break

bc = set()
for i in range(n):
    l = rot[fix[i]][i]
    for p in l:
        bc.add(tuple([p[x]+loc[i][x] for x in range(3)]))
print(len(bc))

