# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0   
        ret = 0
        def dfs(node, mn, mx):
            nonlocal ret
            ret = max(ret, abs(mn - node.val), abs(mx - node.val))
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            for ch in node.left, node.right:
                if ch:
                    dfs(ch, mn, mx)
        dfs(root, root.val, root.val)
        return ret