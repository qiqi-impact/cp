class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        ret = 0
        
        def dfs(idx, p):
            nonlocal ret
            s = set()
            c = 1
            for ch in g[idx]:
                if ch != p:
                    v = dfs(ch, idx)
                    c += v
                    s.add(v)
            if len(s) <= 1:
                ret += 1
            return c
        dfs(0, -1)
        return ret