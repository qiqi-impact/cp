# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, node, l, r):
        if not node:
            return None
        if node.val > r:
            return self.solve(node.left, l, r)
        if node.val < l:
            return self.solve(node.right, l, r)
        node.left = self.solve(node.left, l, r)
        node.right = self.solve(node.right, l, r)
        return node