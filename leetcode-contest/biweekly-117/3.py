class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dp(idx, safe):
            if idx == len(prices):
                return 0
            ret = inf
            if safe >= idx:
                ret = dp(idx+1, safe)
            ret = min(ret, prices[idx] + dp(idx+1, idx + (idx + 1)))
            return ret
        return dp(0, -1)