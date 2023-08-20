class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x:x[1])
        mx = offers[-1][1]+1
        op = 0
        dp = [0] * mx
        for t in range(mx):
            dp[t] = dp[t-1]
            while op < len(offers) and offers[op][1] == t:
                a, b, c = offers[op]
                dp[t] = max((0 if a == 0 else dp[a-1]) + c, dp[t])
                op += 1
        return dp[-1]