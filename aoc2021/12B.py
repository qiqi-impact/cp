from functools import cache
from collections import defaultdict, deque
import math

nm = {}

class Node:
    def __init__(self, name):
        self.name = name
        self.small = (name == name.lower())
        self.adj = []
        self.vis = 2

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

nm['start'].vis = nm['end'].vis = 1

used = False
def dfs(node):
    global ret
    path.append(node.name)
    if node.name == 'end':
        ret += 1
        print(path)
    if node.small:
        node.vis -= 1
    for ch in node.adj:
        if ch.vis > 0:
            dfs(ch)
    if node.small:
        node.vis += 1
    path.pop()

dfs(nm['start'])
print(ret)