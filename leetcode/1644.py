# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret = None
        def dfs(node):
            nonlocal ret
            if not node:
                return set()
            found = dfs(node.left) | dfs(node.right)
            for k in [p, q]:
                if node == k:
                    found.add(k.val)
                    break
            if len(found) == 2 and ret is None:
                ret = node
            return found
        dfs(root)
        return ret