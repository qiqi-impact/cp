class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(idx):
            if idx >= len(prices):
                return 0
            mx = dp(idx+1)
            for j in range(idx+1, len(prices)):
                if prices[j] > prices[idx]:
                    mx = max(mx, prices[j] - prices[idx] + dp(j+2))
            return mx
        return dp(0)