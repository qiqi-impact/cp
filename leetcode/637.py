# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = {}
        
        def dfs(node, level):
            if level not in d:
                d[level] = [0, 0]
            d[level][0] += node.val
            d[level][1] += 1
            for ch in node.left, node.right:
                if ch:
                    dfs(ch, level+1)
        
        dfs(root, 0)
        ret = []
        for i in range(max(d)+1):
            ret.append(d[i][0]/d[i][1])
        return ret