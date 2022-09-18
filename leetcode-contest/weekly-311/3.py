# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = defaultdict(list)
        def dfs(node, depth):
            if not node:
                return
            d[depth].append(node)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root, 0)
        for k in d:
            if k%2 == 1:
                l = d[k]
                for i in range(len(l)//2):
                    a, b = l[i], l[len(l)-1-i]
                    a.val, b.val = b.val, a.val
        return root
                    