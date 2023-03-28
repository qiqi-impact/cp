"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodes = {}
        def dfs(x):
            if x.val in nodes:
                return nodes[x.val]
            n = Node(x.val)
            nodes[n.val] = n
            n.neighbors = [dfs(t) for t in x.neighbors]
            return n
        return dfs(node)
        