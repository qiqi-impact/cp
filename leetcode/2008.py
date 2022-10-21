class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n+1)
        g = [defaultdict(int) for _ in range(n)]
        for x, y, z in rides:
            x -= 1
            y -= 1
            g[x][y] = max(g[x][y], z)
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1]
            for o in g[i]:
                dp[i] = max(dp[i], g[i][o] + o - i + dp[o])
        return dp[0]