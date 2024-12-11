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
        sm = sum(l)
        ll = ['.'] * sm
        ct = 0
        p = 0
        for i in range(len(l)):
            if i % 2 == 0:
                for j in range(l[i]):
                    ll[p] = ct
                    p += 1
                ct += 1
            else:
                p += l[i]
        print(ll)
        
        p = 0
        while p < len(ll) and ll[p] != '.':
            p += 1

        q = len(ll) - 1

        while p < q:
            ll[p], ll[q] = ll[q], ll[p]
            while p < len(ll) and ll[p] != '.':
                p += 1
            while q >= 0 and ll[q] == '.':
                q -= 1
        # print(ll)
ret = 0
for i in range(len(ll)):
    if ll[i] != '.':
        ret += int(ll[i]) * i

print(ret)