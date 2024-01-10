# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(set)
        def dfs(node):
            for ch in node.left, node.right:
                if ch:
                    a, b = node.val, ch.val
                    g[a].add(b)
                    g[b].add(a)
                    dfs(ch)
        dfs(root)

        ret = 0
        seen = set([start])
        q = deque([(0, start)])
        while q:
            x, y = q.popleft()
            for z in g[y]:
                if z not in seen:
                    seen.add(z)
                    q.append((x+1, z))
                    ret = max(ret, x+1)
        return ret