class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ct = 1
        vis = [0] * n
        ret = [0] * n
        
        def dfs(node):
            nonlocal ct
            if ret[node]:
                return node
            if vis[node]:
                ret[node] = ct - vis[node]
                return node
            vis[node] = ct
            ct += 1
            v = ret[edges[node]]
            if v:
                ret[node] = 1 + v
                return node
            end = dfs(edges[node])
            v = ret[edges[node]]
            ret[node] = v
            if vis[node] < vis[end]:
                ret[node] += 1
            return end
        
        for i in range(n):
            if not vis[i]:
                dfs(i)
                
        return ret