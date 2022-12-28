from functools import cache
from collections import defaultdict, deque
import math

nm = {}

class Node:
    def __init__(self, name):
        self.name = name
        self.small = (name == name.lower())
        self.adj = []
        self.vis = False

ret = 0
with open('in') as f:
    for i, l in enumerate(f.read().splitlines()):
        a, b = l.split('-')
        if a not in nm:
            nm[a] = Node(a)
        if b not in nm:
            nm[b] = Node(b)
        nm[a].adj.append(nm[b])
        nm[b].adj.append(nm[a])

def dfs(node):
    global ret
    if node.name == 'end':
        ret += 1
    if node.small:
        node.vis = True
    for ch in node.adj:
        if not ch.vis:
            dfs(ch)
    if node.small:
        node.vis = False

dfs(nm['start'])
print(ret)