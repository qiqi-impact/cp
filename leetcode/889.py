# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inv = {}
        for i, x in enumerate(postorder):
            inv[x] = i

        def dfs(prei, prej, posti, postj):
            pt = prei
            ret = TreeNode(preorder[prei])
            pt += 1
            if pt == prej+1:
                return ret
            ln = inv[preorder[pt]] - posti
            ret.left = dfs(pt, pt + ln, posti, posti + ln)
            pt += ln+1
            if pt == prej+1:
                return ret
            ret.right = dfs(pt, prej, posti + ln + 1, postj)
            return ret

        return dfs(0, len(preorder)-1, 0, len(postorder)-1)