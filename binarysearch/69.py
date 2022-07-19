# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return True
        def dfs(node):
            mn = node.val
            mx = node.val
            if node.left:
                a, b, c = dfs(node.left)
                if not c:
                    return a, b, c
                if b >= node.val:
                    return None, None, False
                mn = a
            if node.right:
                a, b, c = dfs(node.right)
                if not c:
                    return a, b, c
                if a <= node.val:
                    return None, None, False
                mx = b
            return mn, mx, True
        return dfs(root)[2]