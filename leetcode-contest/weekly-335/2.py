# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        d = defaultdict(int)
        def dfs(node, depth):
            d[depth] += node.val
            for ch in node.left, node.right:
                if ch:
                    dfs(ch, depth+1)
        dfs(root, 0)
        # print(d)
        l = sorted(d.values())
        if len(l) < k:
            return -1
        return l[-k]