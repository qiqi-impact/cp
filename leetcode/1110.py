# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root: return []

        roots = []
        std = set(to_delete)
        pr = [root]

        def dfs(node):
            if node.val in std:
                for ch in node.left, node.right:
                    if ch:
                        pr.append(ch)
            for ch in node.left, node.right:
                if ch:
                    dfs(ch)
        dfs(root)

        def dfs2(node):
            if node.left:
                if node.left.val in std:
                    node.left = None
                else:
                    dfs2(node.left)
            if node.right:
                if node.right.val in std:
                    node.right = None
                else:
                    dfs2(node.right)

        ret = []
        for node in pr:
            if node.val not in std:
                dfs2(node)
                ret.append(node)

        return ret
        

