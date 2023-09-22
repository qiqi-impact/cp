from collections import defaultdict

class Node:
    def __init__(self):
        self.ch = []

def count_desc(root, k):
    dc = defaultdict(int)
    
    ex = {}
    ans = {}

    def dfs(node, depth):
        old = dc[depth+k]
        for ch in node.ch:
            dfs(ch, depth+1)
        cur = dc[depth+k]
        ex[node] = cur - old
        dc[depth] += 1

    dfs(root, 0)

    def dfs2(node):
        ret = ex[node]
        for ch in node.ch:
            ret += dfs2(ch)
        ans[node] = ret
        return ret

    dfs2(root)
    return ans

nodes = [Node() for _ in range(15)]
for i in range(7):
    nodes[i].ch = [nodes[2*i+1], nodes[2*i+2]]

d = count_desc(nodes[0], 1)
print([d[x] for x in nodes])