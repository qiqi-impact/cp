# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ret = 0
        def dfs(node):
            nonlocal ret
            if low <= node.val <= high:
                ret += node.val
            if node.val > low and node.left:
                dfs(node.left)
            if node.val < high and node.right:
                dfs(node.right)
        dfs(root)
        return ret