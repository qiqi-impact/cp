from functools import cache
from collections import defaultdict, deque
import math
from fractions import Fraction

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

AA = Fraction(200000000000000, 1)
BB = Fraction(400000000000000, 1)

cur = []
ret = 0
for l in lines:
    x, y = l.split(' @ ')
    a = ints(x, ', ')
    b = ints(y, ', ')
    A, B, C, D = a[0], a[1], b[0], b[1]
    M, Y = Fraction(D, C), Fraction(B*C - A*D, C)
    cur.append([M, Y, A, B, C, D])
    # print(A, B, C, D)

for i in range(len(cur)):
    for j in range(i+1, len(cur)):
        if cur[i][0] != cur[j][0]:
            x = Fraction(cur[i][1] - cur[j][1], cur[j][0] - cur[i][0])
            y = cur[i][0] * x + cur[i][1]
            # print(i, j, x, y)
            if AA <= x <= BB and AA <= y <= BB:
                wa = Fraction(y - cur[i][3], cur[i][5])
                wb = Fraction(y - cur[j][3], cur[j][5])
                if wa >= 0 and wb >= 0:
                    ret += 1
print(ret)

