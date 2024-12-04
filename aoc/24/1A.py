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
# L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
# DIR = [R, D, L, U]

lines = []
ret = 0
with open("in") as f:
    t, y = [], []
    ct = {}
    for a in f.read().splitlines():
        lines.append(a)
        x = a.split('  ')
        t.append(int(x[0]))
        ct[int(x[1])] = ct.get(int(x[1]), 0) + 1
    for i in range(len(t)):
        ret += t[i] * ct.get(t[i], 0)
print(ret)
ln = len(lines)