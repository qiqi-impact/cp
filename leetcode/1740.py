# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        ret = None
        def dfs(node):
            nonlocal ret
            if not node: return -1
            a = dfs(node.left)
            b = dfs(node.right)
            if a == -1 and b == -1:
                if node.val == p or node.val == q:
                    return 0
                return -1
            elif a == -1:
                if node.val == p or node.val == q:
                    ret = b + 1
                    return -1
                return b + 1
            elif b == -1:
                if node.val == p or node.val == q:
                    ret = a + 1
                    return -1
                return a + 1
            else:
                ret = a + b + 2
                return -1
        dfs(root)
        return ret