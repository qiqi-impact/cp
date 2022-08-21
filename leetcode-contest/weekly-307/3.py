# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = defaultdict(list)
        
        def dfs(node):
            for ch in node.left, node.right:
                if ch:
                    g[node.val].append(ch.val)
                    g[ch.val].append(node.val)
                    dfs(ch)
        
        dfs(root)
        ret = 0
        
        def f(idx, depth, p):
            nonlocal ret
            ret = max(ret, depth)
            for ch in g[idx]:
                if ch != p:
                    f(ch, depth+1, idx)
                
        f(start, 0, -1)
        return ret