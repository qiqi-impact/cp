# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        l = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            l.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        
        ret = []
        for q in queries:
            idx = bisect.bisect_left(l, q)
            mn = 1e9
            mx = -1e9
            for x in range(idx-1, idx+1):
                if 0 <= x < len(l):
                    if l[x] <= q:
                        mx = max(mx, l[x])
                    if l[x] >= q:
                        mn = min(mn, l[x])
            if mn == 1e9: mn = -1
            if mx == -1e9: mx = -1
            ret.append([mx, mn])
        return ret