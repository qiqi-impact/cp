class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        vis = [0] * n
        
        ret = -1
        
        def dfs(idx, depth):
            nonlocal ret
            if edges[idx] == -1:
                pass
            elif vis[edges[idx]] > 0:
                ret = max(ret, depth+1 - vis[edges[idx]])
            elif vis[edges[idx]] != -1:
                vis[idx] = depth
                dfs(edges[idx], depth+1)
            vis[idx] = -1
        
        for i in range(n):
            if vis[i] == 0:
                dfs(i, 1)
                
        return ret