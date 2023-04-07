# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        
        def dfs(node, depth):
            d[depth].append(node.val)
            for ch in node.left, node.right:
                if ch:
                    dfs(ch, depth+1)
                    
        dfs(root, 0)
        
        ret = 0
        
        for k in d:
            l = d[k]
            r = sorted(l)
            
            g = {}
            for i in range(len(l)):
                g[l[i]] = r[i]
            
            vis = set()
            for x in g:
                ct = 0
                while x not in vis:
                    ct += 1
                    vis.add(x)
                    x = g[x]
                ret += max(0, ct - 1)
        return ret