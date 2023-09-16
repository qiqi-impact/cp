class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        ag = [[] for _ in range(n)]
        g = [set() for _ in range(n)]
        
        for x, y in edges:
            g[x].add(y)
            ag[x].append(y)
            ag[y].append(x)
        
        ret = [None] * n
        def dfs(node, p):
            r = 0
            for x in ag[node]:
                if x != p:
                    if x not in g[node]:
                        r += 1
                    r += dfs(x, node)
            return r
        
        def dfs2(node, p, v):
            ret[node] = v
            for x in ag[node]:
                if x != p:
                    df = 1 if x in g[node] else -1
                    dfs2(x, node, v + df)
        dfs2(0, -1, dfs(0, -1))
        return ret
            
                    