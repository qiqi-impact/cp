class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(edges)+1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        @cache
        def dfs(idx, p, nz):
            ct = 0
            for x in g[idx]:
                if x != p:
                    ct += 1
            if ct == 0 and not nz:
                return 0
            a = 0
            for x in g[idx]:
                if x != p:
                    a += dfs(x, idx, True)
            b = values[idx]
            for x in g[idx]:
                if x != p:
                    b += dfs(x, idx, nz)
            return max(a, b)
        return dfs(0, -1, False)
            