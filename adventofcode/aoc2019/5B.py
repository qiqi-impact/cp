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
# ln = len(lines)

def f(ip):
    l = lines[0].split(',')

    def g(idx, p):
        nonlocal m
        return int(l[idx]) if m[p] == '0' else idx

    def params(ct):
        nonlocal m, pt
        x = [int(y) for y in l[pt+1:pt+ct+1]]
        print(x, m)
        pr = [g(x[i], i) for i in range(ct)]
        print(pr)
        return pr

    pt = 0
    out = None
    while 1:
        v = l[pt]
        v = '0' * (5 - len(v)) + v
        print(v)
        op = v[-2:]
        m = [x for x in v[:-2][::-1]]
        if op == '99':
            break
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
            l[a] = str(ip)
            pt += 2
        elif op == '04':
            [a] = params(1)
            out = a
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
        # print(l[:10], pt)
        # input()
    print(l, out)

f(5)