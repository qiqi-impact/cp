# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        depths = defaultdict(list)
        def dfs(node, d):
            depths[d].append(node.val)
            for ch in node.left, node.right:
                if ch:
                    dfs(ch, d+1)
        dfs(root, 0)
        
        ret = 0
        
        for k in depths:
            l = depths[k]
            r = sorted(l)
            # print(k, l, r)
            m = {}
            for i, x in enumerate(l):
                m[x] = r[i]
            vis = set()
            for t in m:
                if t not in vis:
                    q = 0
                    cur = t
                    while m[cur] not in vis:
                        vis.add(m[cur])
                        cur = m[cur]
                        q += 1
                    # print(t, q)
                    ret += q - 1
        return ret