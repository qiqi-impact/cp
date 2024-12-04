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
        x = ints(a)
        A, B = sorted(x), sorted(x, reverse=True)
        if tuple(x) == tuple(A):
            r = 1
            for i in range(len(A)-1):
                if 0 == abs(A[i+1] - A[i]) or 4 <= abs(A[i+1] - A[i]):
                    r = 0
        elif tuple(x) == tuple(B):
            r = 1
            for i in range(len(B)-1):
                if 0 == abs(B[i+1] - B[i]) or 4 <= abs(B[i+1] - B[i]):
                    r = 0
        else:
            r = 0
        ret += r


print(ret)
# ln = len(lines)