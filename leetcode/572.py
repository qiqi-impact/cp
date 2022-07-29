# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        h = None
        found = None
        
        def dfs(node):
            nonlocal found, h
            cur = '-'
            if node:
                cur =  str(node.val) + '/' + dfs(node.left) + '/' + dfs(node.right)
            if cur == h:
                found = True
            return cur
        
        h = dfs(subRoot)
        dfs(root)
        return found