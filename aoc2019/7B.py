from functools import cache
from collections import defaultdict, deque
import math, itertools

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
# ln = len(lines)

def step(t):
    l = st[t]
    def g(idx, p):
        return int(l[idx]) if m[p] == '0' else idx

    def params(ct):
        x = [int(y) for y in l[pt+1:pt+ct+1]]
        # print(x, m)
        pr = [g(x[i], i) for i in range(ct)]
        # print(pr)
        return pr

    pt = ptr[t]
    v = l[pt]
    v = '0' * (5 - len(v)) + v
    # print(v)
    op = v[-2:]
    m = [x for x in v[:-2][::-1]]
    if op == '99':
        h[t] = 1
        return
    elif op == '01':
        m[2] = '1'
        [a, b, c] = params(3)
        l[c] = str(a + b)
        pt += 4
    elif op == '02':
        m[2] = '1'
        [a, b, c] = params(3)
        l[c] = str(a * b)
        pt += 4
    elif op == '03':
        m[0] = '1'
        [a] = params(1)
        if Q[t]:
            l[a] = str(Q[t].popleft())
            pt += 2
    elif op == '04':
        [a] = params(1)
        Q[(t+1)%5].append(a)
        pt += 2
    elif op == '05':
        [a, b] = params(2)
        if a:
            pt = b
        else:
            pt += 3
    elif op == '06':
        [a, b] = params(2)
        if not a:
            pt = b
        else:
            pt += 3
    elif op == '07':
        m[2] = '1'
        [a, b, c] = params(3)
        l[c] = str(int(a < b))
        pt += 4
    elif op == '08':
        m[2] = '1'
        [a, b, c] = params(3)
        l[c] = str(int(a == b))
        pt += 4
    ptr[t] = pt

ret = 0
for x in itertools.permutations('98765'):
    st = [lines[0].split(',') for _ in range(5)]
    Q = [deque([int(x[i])]) for i in range(5)]
    h = [0] * 5
    ptr = [0] * 5
    Q[0].append(0)

    cur = 0
    while 1:
        for i in range(5):
            if not h[i]:
                step(i)
        if sum(h) == 5:
            break
    ret = max(ret, Q[0][-1])
print(ret)