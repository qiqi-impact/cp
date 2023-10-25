class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(idx, state):
            if state == 0 or idx == len(prices):
                return 0
            if state == 1 or state == 3:
                return max(dp(idx+1, state), prices[idx] + dp(idx+1, state-1))
            else:
                return max(dp(idx+1, state), -prices[idx] + dp(idx+1, state-1))
        return dp(0, 4)