# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ret = inf
        def dfs(node):
            nonlocal ret
            a, b = node.val, node.val
            for ch in node.left, node.right:
                if ch:
                    l, r = dfs(ch)
                    a = min(a, l)
                    b = max(b, r)
                    ret = min(ret, abs(node.val - l), abs(node.val - r))
            return a, b
        dfs(root)
        return ret