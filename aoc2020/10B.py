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

ls = [0] + sorted([int(x) for x in lines])

@cache
def dp(idx):
    if idx == len(ls)-1:
        return 1
    c = ls[idx]
    ret = 0
    for j in range(idx+1, len(ls)):
        v = ls[j]
        if v > c + 3:
            break
        ret += dp(j)
    return ret

print(dp(0))