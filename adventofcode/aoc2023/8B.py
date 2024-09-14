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

d = {}
for l in lines[2:]:
    a, b = l.split(' = ')
    x, y = b[1:-1].split(', ')
    d[a] = [x, y]

# print(d)

@cache
def f(t, u):
    cur = t
    ct = 0
    inst = lines[0]
    for i in range(100000):
        c = inst[ct%len(inst)]
        if c == 'L':
            cur = d[cur][0]
        else:
            cur = d[cur][1]
        ct += 1
        if cur == u:
            break
    if ct < 100000: print(t, u, ct)
    return ct if ct < 100000 else int(1e30)

A = []
for k in d:
    if k[-1] == 'A':
        A.append(k)

B = []
for k in d:
    if k[-1] == 'Z':
        B.append(k)

taken = [0] * len(B)
vals = []

print(A, B)

ret = 1e18
def perm(idx):
    global ret
    if idx == len(A):
        ll = []
        for i in range(len(A)):
            # print(A[i], B[vals[i]])
            ll.append(f(A[i], B[vals[i]]))
        # print(ll)
        ret = min(ret, math.lcm(*ll))
    else:
        for i in range(len(B)):
            if not taken[i]:
                vals.append(i)
                taken[i] = 1
                perm(idx+1)
                taken[i] = 0
                vals.pop()
perm(0)
print(ret)