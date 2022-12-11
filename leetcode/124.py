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
            if not node:
                return 0
            lp = max(0, dfs(node.left))
            rp = max(0, dfs(node.right))
            ret = max(ret, node.val + lp + rp)
            return node.val + max(lp, rp)
        dfs(root)       
        return ret