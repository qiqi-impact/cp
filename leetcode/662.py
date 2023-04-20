# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        def dfs(node, depth, n):
            if depth not in d:
                d[depth] = [n, n]
            d[depth][1] = n
            if node.left:
                dfs(node.left, depth+1, 2*n)
            if node.right:
                dfs(node.right, depth+1, 2*n+1)
        dfs(root, 0, 0)
        ret = 0
        for k in d:
            ret = max(ret, d[k][1] - d[k][0])
        return ret + 1