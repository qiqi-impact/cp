# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def f(node):
            nonlocal ans
            ret = []
            if node in [p, q]:
                ret.append(node)
            for ch in node.left, node.right:
                if ch:
                    ret += f(ch)
            if len(ret) == 2 and ans is None:
                ans = node
            return ret
        f(root)
        return ans