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


@cache
def dp(s, r, si, ri, cur):
    # print(s, r, si, ri, cur)
    
    if si == len(s):
        if ri != len(r):
            return 0
        return 1

    v = s[si]
    opts = [1, 0]
    if v == '#':
        opts = [1]
    elif v == '.':
        opts = [0]

    if ri == len(r):
        if 0 not in opts:
            return 0
        return dp(s, r, si+1, ri, 0)
    
    ret = 0
    # print(ret)
    if 0 in opts:
        if cur == r[ri]:
            ret += dp(s, r, si+1, ri+1, 0)
        if cur == 0:
            ret += dp(s, r, si+1, ri, 0)
    if 1 in opts:
        ret += dp(s, r, si+1, ri, cur+1)

    # print(s, r, si, ri, cur, ret)
    return ret

q = 0
for l in lines:
    a, b = l.split(' ')
    b = ints(b, ',')
    print(a, b)
    
    x = dp(a+'.', tuple(b), 0, 0, 0)
    print(x)
    q += x
print(q)