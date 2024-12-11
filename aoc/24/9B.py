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

# dirmap = {
#     'R': [0, 1],
#     'L': [0, -1],
#     'U': [-1, 0],
#     'D': [1, 0],
# }
# L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
# DIR = [R, D, L, U]

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        l = [int(c) for c in str(a)]

        fs, gs = l[::2], l[1::2]

        gm = defaultdict(list)
        skip = set()
        for i in range(len(fs)-1, -1, -1):
            x = fs[i]
            for j in range(min(i, len(gs))):
                if gs[j] >= x:
                    gs[j] -= x
                    gm[j].append((i, x))
                    skip.add(i)
                    break
        ret = 0
        p = 0
        for i in range(len(fs)):
            if i not in skip:
                for j in range(fs[i]):
                    ret += i * p
                    p += 1
            else:
                p += fs[i]
            if i < len(gs):
                s = gs[i]
                for x, y in gm[i]:
                    for j in range(y):
                        ret += x * p
                        p += 1
                p += s

        print(ret)


