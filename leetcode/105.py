# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        m = {}
        for i in range(n):
            m[inorder[i]] = i

        def dfs(pl, pr, il, ir):
            root = preorder[pl]
            mid = m[root]
            node = TreeNode(root)
            if il != mid:
                npl = pl + 1
                npr = npl + mid - il - 1
                node.left = dfs(npl, npr, il, mid-1)
                pl = npr
            if ir != mid:
                npl = pl + 1
                npr = npl + ir - mid - 1
                node.right = dfs(npl, npr, mid+1, ir)
            return node

        return dfs(0, n-1, 0, n-1)