class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            w -= 1
            g[x].append((y, w))
            g[y].append((x, w))
        
        p = [[0 for _ in range(n)]]
        depth = [0] * n
        
        cum = [None for _ in range(n)]
        
        cw = [0] * 26
        def dfs(x, q, dp):
            p[0][x] = q
            depth[x] = dp
            cum[x] = cw[:]
            for ch, w in g[x]:
                if ch != q:
                    cw[w] += 1
                    dfs(ch, x, dp+1)
                    cw[w] -= 1
        dfs(0, 0, 0)
        
        MX = 14
        
        for _ in range(MX):
            pp = [p[-1][p[-1][i]] for i in range(n)]
            p.append(pp)
        
        def lca(x, y):
            if depth[x] < depth[y]:
                x, y = y, x
            l, r = depth[x]-depth[y], depth[x]
            while l < r:
                mi = (l+r)//2
                a, b = x, y
                for i in range(MX):
                    if mi & (1 << i):
                        a = p[i][a]
                for i in range(MX):
                    if (mi-(depth[x]-depth[y])) & (1 << i):
                        b = p[i][b]
                if a == b:
                    r = mi
                else:
                    l = mi+1
            for i in range(MX):
                if r & (1 << i):
                    x = p[i][x]
            return x
        
        ret = []
        for a, b in queries:
            t = lca(a, b)
            y = [0] * 26
            for i in range(26):
                y[i] = cum[a][i] + cum[b][i] - 2 * cum[t][i]
            ret.append(sum(y) - max(y))
        return ret
            
            