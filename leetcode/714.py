class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, j):
            if i == len(prices):
                return 0
            if j == 0:
                a = dp(i+1, 0)
                b = -prices[i] + dp(i+1, 1)
                return max(a, b)
            else:
                a = dp(i+1, 1)
                b = prices[i] - fee + dp(i+1, 0)
                return max(a, b)
        return dp(0, 0)