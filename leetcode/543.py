# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def dfs(node):
            nonlocal ret
            ans = 0
            if node.left:
                l = dfs(node.left)
                ans = max(ans, l+1)
                ret = max(ret, ans)
            if node.right:
                r = dfs(node.right)
                ans = max(ans, r+1)
                ret = max(ret, ans)
            if node.left and node.right:
                ret = max(ret, l+r+2)
            return ans
        dfs(root)
        return ret