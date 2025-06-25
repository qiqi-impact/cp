class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ret = 0
        def dfs(node, p):
            nonlocal ret
            mx = 0
            d = defaultdict(int)
            ct = 0
            for ch in g[node]:
                if ch != p:
                    v = dfs(ch, node)
                    mx = max(mx, v)
                    d[v] += 1
                    ct += 1
            ret += ct - d[mx]
            return cost[node] + mx

        dfs(0, -1)
        return ret©leetcode