from functools import cache
from collections import defaultdict, deque
import math

nm = {}

class Node:
    def __init__(self, name):
        self.name = name
        self.small = (name == name.lower())
        self.adj = []
        self.vis = 0

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

used = False
# path = []
def dfs(node):
    global ret, used
    # path.append(node.name)
    if node.name == 'end':
        ret += 1
        # print(path)
    if node.small:
        node.vis += 1
    for ch in node.adj:
        if not ch.vis:
            dfs(ch)
        elif ch.vis == 1 and ch.name not in ['start', 'end'] and not used:
            used = True
            dfs(ch)
            used = False
    if node.small:
        node.vis -= 1
    # path.pop()

dfs(nm['start'])
print(ret)