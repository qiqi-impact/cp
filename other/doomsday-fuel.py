import math
from fractions import Fraction

def apply(m, v):
    n = len(v)
    nv = [0] * n
    for i in range(n):
        for j in range(n):
            nv[i] += v[j] * m[j][i]
    return nv


M = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

norm = []
for i, r in enumerate(M):
    s = sum(r)
    if s == 0:
        t = [Fraction(0, 1)] * len(r)
        t[i] = Fraction(1, 1)
        norm.append(t)
    else:
        norm.append([Fraction(x, s) for x in r])

# print(norm)
v = [0] * len(M)
v[0] = 1
for i in range(100):
    same = 0
    cv = apply(norm, v)
    for j in range(len(M)):
        if v[j] == cv[j]:
            same += 1
    if same == len(M):
        break
    v = cv

d = 1
for f in v:
    d = math.lcm(d, f.denominator)

ret = []
for f in v:
    ret.append(f.numerator * d // f.denominator)
ret.append(d)

print(ret)