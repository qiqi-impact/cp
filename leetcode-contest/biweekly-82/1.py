# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.val <= 1:
                return bool(node.val)
            elif node.val == 2:
                return dfs(node.left) or dfs(node.right)
            else:
                return dfs(node.left) and dfs(node.right)
        return dfs(root)