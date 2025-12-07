class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        below = [None] * n
        def dfs(idx, p):
            sm = 1 if good[idx] else -1
            for ch in g[idx]:
                if ch != p:
                    q = dfs(ch, idx)
                    if q > 0:
                        sm += q
            below[idx] = sm
            return sm
            
        ret = [None] * n
        def trav(idx, p, tot):
            if p == -1:
                cur = 0
            else:
                cur = ret[p]
                if below[idx] > 0:
                    cur -= below[idx]
            ret[idx] = below[idx] + max(cur, 0)
            nt = (1 if good[idx] else -1) + max(tot, 0)
            for ch in g[idx]:
                if ch != p:
                    trav(ch, idx, nt)

        dfs(0, -1)
        trav(0, -1, 0)
        return ret