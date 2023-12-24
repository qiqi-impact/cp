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

def copy_blob(q):
    if not q: return q
    return {k:q[k][:] for k in q}

def chop_blob(q, k, op, v):
    if not q: return q, q
    a, b = q[k]
    q = copy_blob(q)
    r = copy_blob(q)
    if op == '>':
        if v >= b:
            return q, None
        if v >= a:
            q[k] = [a, v]
            r[k] = [v+1, b]
    else:
        if v <= a:
            return q, None
        if v <= b:
            q[k] = [v, b]
            r[k] = [a, v-1]
    return q, r

def process(blob, cur):
    # print(blob, cur)
    global ret
    if cur == 'R' or not blob:
        return
    if cur == 'A':
        p = 1
        for v in blob.values():
            p *= v[1] - v[0] + 1
        ret += p
        return
    for r in d[cur]:
        if len(r) == 1:
            process(blob, r[0])
        else:
            blob, new_blob = chop_blob(blob, r[0], r[1], r[2])
            process(new_blob, r[3])


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
        root = {'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]}
        process(root, 'in')
        break
print(ret)

