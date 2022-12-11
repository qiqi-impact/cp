# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = -1e9
        
        def dfs(node):
            nonlocal ret
            paths = []
            for ch in node.left, node.right:
                if ch:
                    paths.append(dfs(ch))
            d = node.val
            ret = max(ret, d)
            for p in paths:
                d = max(d, node.val + p)
                ret = max(ret, d)
            if len(paths) == 2:
                ret = max(ret, node.val + sum(paths))
            return d
        dfs(root)
        
        return ret