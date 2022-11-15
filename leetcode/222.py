# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def fh(node):
            if node.left:
                return 1 + fh(node.left)
            return 0
        
        if not root: return 0
        
        depth = fh(root)
        
        def can(x):
            cur = root
            for i in range(depth-1, -1, -1):
                if x & (1 << i):
                    nx = cur.right
                else:
                    nx = cur.left
                if not nx:
                    return False
                cur = nx
            return True
        
        l, r = 0, 2**depth-1
        while l < r:
            mi = (l+r+1)//2
            v = can(mi)
            if v:
                l = mi
            else:
                r = mi - 1
        return l+(2**depth)