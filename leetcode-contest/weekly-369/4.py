class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        @cache
        def dp(idx, p, f):
            ret = (coins[idx] >> f) - k
            for o in g[idx]:
                if o != p:
                    ret += dp(o, idx, min(f, 16))
            
            q = coins[idx] >> (f+1)
            for o in g[idx]:
                if o != p:
                    q += dp(o, idx, min(f+1, 16))
            return max(ret, q)
        
        return dp(0, -1, 0)