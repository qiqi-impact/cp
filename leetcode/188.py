class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        g = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):
                v = prices[j] - prices[i]
                if v > 0 and (not g[i] or g[i][-1][0] < v):
                    g[i].append((v, j))
        
        @cache
        def dp(idx, left):
            if idx == n:
                return 0
            if left == 0:
                return 0
            ret = dp(idx+1, left)
            for (v, j) in g[idx]:
                ret = max(ret, v + dp(j+1, left-1))
            return ret
        
        return dp(0, k)