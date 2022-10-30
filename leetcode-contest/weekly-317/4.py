# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        d = {}
        def dfs(node):
            ret = [0, 0]
            if node.left or node.right:
                for i, ch in enumerate([node.left, node.right]):
                    if ch:
                        ret[i] = 1 + max(dfs(ch))
            d[node.val] = ret
            return ret
        dfs(root)

        ans = {}
        def dfs2(node, mx, step):
            if not node: return
            ans[node.val] = mx
            dfs2(node.left, max(mx, step + d[node.val][1]), step + 1)
            dfs2(node.right, max(mx, step + d[node.val][0]), step + 1)

        dfs2(root.left, d[root.val][1], 1)
        dfs2(root.right, d[root.val][0], 1)
        return [ans[x] for x in queries]