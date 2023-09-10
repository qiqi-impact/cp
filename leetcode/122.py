class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, b):
            if i == len(prices):
                return 0
            if b == 0:
                x = dp(i+1, 0)
                y = -prices[i] + dp(i+1, 1)
                return max(x, y)
            else:
                x = dp(i+1, 1)
                y = prices[i] + dp(i+1, 0)
                return max(x, y)
        return dp(0, 0)