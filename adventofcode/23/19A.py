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

dirmap = {
    'R': [0, 1],
    'L': [0, -1],
    'U': [-1, 0],
    'D': [1, 0],
}
L, R, U, D = [[0,-1], [0,1], [-1,0], [1,0]]
DIR = [R, D, L, U]

lines = []
with open("in") as f:
    for a in f.read().splitlines():
        lines.append(a)
ln = len(lines)

step = 0

d = {}
ret = 0
for l in lines:
    if not l.strip():
        step += 1
        continue
    if step == 0:
        name, b = l.split('{')
        rules = []
        for x in b[:-1].split(','):
            if ':' not in x:
                rules.append([x])
                continue
            rule, dst = x.split(':')
            for k in '<>':
                if k in rule:
                    xx, yy = rule.split(k)
                    ru = [xx, k, int(yy), dst]
                    rules.append(ru)
        d[name] = rules
    else:
        st = {}
        print(l)
        for x in l[1:-1].split(','):
            a, b = x.split('=')
            st[a] = int(b)
        cur = 'in'
        while cur not in ['A', 'R']:
            for r in d[cur]:
                if len(r) == 1:
                    cur = r[0]
                else:
                    if r[1] == '>' and st[r[0]] > r[2]:
                        cur = r[3]
                        break
                    elif r[1] == '<' and st[r[0]] < r[2]:
                        cur = r[3]
                        break
        if cur == 'A':
            ret += sum(st.values())
print(ret)

