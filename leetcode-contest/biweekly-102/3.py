# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        
        sm = defaultdict(int)
        def get_sum(node, depth):
            sm[depth] += node.val
            for ch in node.left, node.right:
                if ch:
                    get_sum(ch, depth+1)
        get_sum(root, 0)
        
        def dfs(node, depth):
            cur = 0
            for ch in node.left, node.right:
                if ch:
                    cur += ch.val
            for ch in node.left, node.right:
                if ch:
                    ch.val = sm[depth+1] - cur
                    dfs(ch, depth+1)
        dfs(root, 0)
        
        return root