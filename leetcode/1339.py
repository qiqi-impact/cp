# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        l = []
        def dfs(node):
            ret = node.val
            for ch in node.left, node.right:
                if ch:
                    ret += dfs(ch)
            l.append(ret)
            return ret
        dfs(root)
        ret = 0
        for i in range(len(l)-1):
            ret = max(ret, (l[-1] - l[i]) * l[i])
        return ret % (10**9+7)