# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        def dfs(node):
            if not node: return 0
            ret = node.val
            for ch in node.left, node.right:
                ret += dfs(ch)
            freq[ret] += 1
            return ret
        dfs(root)
        mx = 0
        mxv = []
        for k, v in freq.items():
            if v > mx:
                mx = v
                mxv = [k]
            elif v == mx:
                mxv.append(k)
        return mxv