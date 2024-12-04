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

    def g(idx, m, p):
        return int(l[idx]) if (p >= len(m) or m[p] == '0') else idx

    pt = 0
    out = None
    while 1:
        v = l[pt]
        op = v[-2:]
        if len(op) < 2:
            op = '0' + op
        m = v[:-2][::-1]
        if op == '99':
            break
        elif op == '01':
            [a, b, c] = [int(x) for x in l[pt+1:pt+4]]
            print(a, b, c)
            l[c] = str(g(a, m, 0) + g(b, m, 1))
            pt += 4
        elif op == '02':
            [a, b, c] = [int(x) for x in l[pt+1:pt+4]]
            print(a, b, c)
            l[c] = str(g(a, m, 0) * g(b, m, 1))
            pt += 4
        elif op == '03':
            [a] = [int(x) for x in l[pt+1:pt+2]]
            
            l[a] = str(ip)
            print(a, l[a])
            pt += 2
        elif op == '04':
            [a] = [int(x) for x in l[pt+1:pt+2]]
            out = g(a, m, 0)
            pt += 2
        print(l[:10], pt)
        # input()
    print(l, out)

f(1)