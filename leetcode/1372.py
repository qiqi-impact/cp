# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def dfs(node):
            '''
            return [longest path starting with left from this node, longest path starting with right from this node]
            '''
            nonlocal mx
            a = dfs(node.left) if node.left else [-1, -1]
            b = dfs(node.right) if node.right else [-1, -1]
            ret = [1 + a[1], 1 + b[0]]
            mx = max(mx, ret[0], ret[1])
            return ret
        dfs(root)
        return mx