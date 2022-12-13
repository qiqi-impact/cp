# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if not node.left and not node.right:
                arr.append(node.val)
            for ch in node.left, node.right:
                if ch:
                    dfs(ch, arr)
        l, r = [], []
        dfs(root1, l)
        dfs(root2, r)
        return l == r