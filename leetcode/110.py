# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret = True
        def depth(node):
            nonlocal ret
            l = []
            for ch in node.left, node.right:
                if ch:
                    l.append(depth(ch))
            # this special case is not explained in the problem statement
            while len(l) < 2:
                l.append(-1)
            if len(l) == 2 and abs(l[0] - l[1]) > 1:
                ret = False
            return 1 + max(l)
        if root: depth(root)
        return ret