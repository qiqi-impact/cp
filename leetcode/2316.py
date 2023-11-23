class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        vis = [0] * n
        def dfs(i):
            vis[i] = 1
            ret = 1
            for o in g[i]:
                if not vis[o]:
                    ret += dfs(o)
            return ret

        ans = 0
        for i in range(n):
            if not vis[i]:
                q = dfs(i)
                ans += q * (n - q)
        return ans // 2