from functools import cache
from collections import defaultdict, deque
import math, sys

sys.setrecursionlimit(10000)

import networkx

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
R = len(lines)

g = networkx.Graph()
comp = set()
for x in lines:
    a, b = x.split(': ')
    comp.add(a)
    for c in b.split(' '):
        g.add_edge(a, c)
        comp.add(c)

for x, y in networkx.minimum_edge_cut(g):
    g.remove_edge(x, y)

print([len(c) for c in networkx.connected_components(g)])