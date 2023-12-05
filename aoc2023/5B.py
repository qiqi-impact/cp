from functools import cache
from collections import defaultdict, deque
import math

def ints(s, split=' '):
    return [int(x) for x in s.split(split) if x]

def colon(s):
    return s.split(': ')[1]

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digmap = {}
for i, x in enumerate(digits):
    digmap[x] = i

ret = []
ct = 0
maps = []
r = []
with open("in") as f:
    for a in f.read().splitlines() + ['']:
        ct += 1
        if ct == 1:
            seeds = ints(colon(a))
            # print(seeds)
        elif a == '':
            if r:
                r.sort()
                maps.append(r)
                r = []
        elif ':' not in a:
            x, y, z = ints(a)
            r.append([y, y+z-1, x - y])

cur = []
for i in range(0, len(seeds)-1, 2):
    cur.append([seeds[i], seeds[i]+seeds[i+1]-1])

# print(cur)
# print(maps)

for m in maps:
    nc = []
    ev = defaultdict(list)
    for (x, y) in cur:
        ev[x].append((1, 1, None))
        ev[y].append((1, -1, None))
    for i, (x, y, d) in enumerate(m):
        ev[x].append((0, 1, i))
        ev[y].append((2, -1, i))
    ks = sorted(ev.keys())
    # print(1)

    L = None
    df = 0
    for k in ks:
        # print(k)
        l = sorted(ev[k])
        for x, y, i in l:
            # print(x, y, z)
            if x == 0:
                df += m[i][2]
                if L is not None:
                    nc.append([L, m[i][0]-1])
                    L = m[i][0]+df
            elif x == 2:
                if L is not None:
                    nc.append([L, m[i][1]+df])
                    L = m[i][1]+1
                df -= m[i][2]
            elif x == 1:
                if y == 1:
                    L = k+df
                else:
                    nc.append([L, k+df])
                    L = None
            # print(df, L, nc)
    cur = nc
    # print(m)
    # print(cur)

    ev = defaultdict(int)
    for x, y in cur:
        ev[x] += 1
        ev[y+1] -= 1
    ks = sorted(ev.keys())
    st = 0

    cur = []
    for k in ks:
        st += ev[k]
        if st > 0 and st-ev[k] == 0:
            cur.append([k, None])
        elif st == 0 and st-ev[k] > 0:
            cur[-1][1] = k-1
    # print(cur)


            

print(min(cur[0]))

