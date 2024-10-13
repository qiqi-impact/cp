# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        l = []

        def dfs(node):
            if not node: return -1
            a, b = node.left, node.right
            if not a and not b:
                l.append(1)
                return 1
            c, d = dfs(a), dfs(b)
            if a and b and c == d and c != -1:
                l.append(2 * c + 1)
                return 2 * c + 1
            return -1
        dfs(root)
        l.sort(reverse=True)
        k -= 1
        if k >= len(l):
            return -1
        return l[k]