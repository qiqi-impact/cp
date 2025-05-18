class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MX = 32
        n = len(edges) + 1

        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))
        
        depth = [0] * n
        wd = [0] * n
        p = [[0 for _ in range(n)]]
        
        def dfs(x, q, dp, wdp):
            p[0][x] = q
            depth[x] = dp
            wd[x] = wdp
            for ch, w in g[x]:
                if ch != q:
                    dfs(ch, x, dp+1, wdp + w)
        dfs(0, 0, 0, 0)
        
        for _ in range(MX):
            pp = [p[-1][p[-1][i]] for i in range(n)]
            p.append(pp)
        
        def lca(x, y):
            if depth[x] < depth[y]:
                x, y = y, x
            for i in range(MX):
                if (depth[x]-depth[y]) & (1 << i):
                    x = p[i][x]
            if x == y:
                return x
            for i in range(MX-1, -1, -1):
                if p[i][x] != p[i][y]:
                    x, y = p[i][x], p[i][y]
            return p[0][x]

        def lcaw(a, b):
            return wd[a] + wd[b] - 2 * wd[lca(a, b)]

        ret = []
        for a, b, c in queries:
            ret.append((lcaw(a, b) + lcaw(a, c) + lcaw(b, c)) //2 )
        return ret