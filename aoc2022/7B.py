from functools import cache

class Node:
    def __init__(self, name, p):
        self.name = name
        self.sz = 0
        self.ch = {}
        self.parent = p

# @cache
# def size(node):
#     a = node.sz
#     b = sum([size(dirs[x]) for x in node.dir])
#     return a + b

root = Node('/', None)
cur = root
with open('in') as f:
    for x in f.read().splitlines():
        if x[0:4] == '$ cd':
            n = x[5:]
            if n == '/':
                cur = root
            elif n == '..':
                if cur == root:
                    continue
                cur = cur.parent
            else:
                cur = cur.ch[n]
        elif x[0:4] == '$ ls':
            pass
        elif x.startswith('dir'):
            n = x[4:]
            if n not in cur.ch:
                cur.ch[n] = Node(n, cur)
        else:
            cur.sz += int(x.split()[0])

ret = 1e9
tot = 0
def dfs(node, b):
    global ret, tot
    cs = node.sz
    for child in node.ch:
        v = dfs(node.ch[child], b)
        cs += v
    if b and (70000000 - tot + cs >= 30000000):
        ret = min(ret, cs)
    return cs

tot = dfs(root, False)
dfs(root, True)
print(ret)
            


