class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        edges = [[x-1, y-1] for x, y in edges]
        
        n = len(edges)
        g = [set() for _ in range(n)]
        ind = [0] * n
        src = set(range(n))
        for x, y in edges:
            if y in g[x]:
                return [x+1, y+1]
            g[x].add(y)
            ind[y] += 1
            src.discard(y)
            
        def dfs(idx):
            nonlocal vis
            vis.add(idx)
            for o in g[idx]:
                if o not in vis:
                    dfs(o)
            
        for i in range(n-1, -1, -1):
            x, y = edges[i]
            g[x].discard(y)
            ind[y] -= 1
            if ind[y] == 0:
                src.add(y)
                
            if len(src) == 1:
                vis = set()
                dfs(list(src)[0])
                if len(vis) == n:
                    return [x+1, y+1]
            if ind[y] == 0:
                src.discard(y)
            ind[y] += 1
            g[x].add(y)