# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node, subnode):
            if subnode is None:
                return node is None
            if node is None:
                return False
            if node.val != subnode.val:
                return False
            return check(node.left, subnode.left) and check(node.right, subnode.right)
        
        def dfs(node):
            if check(node, subRoot):
                return True
            if not node: return False
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)