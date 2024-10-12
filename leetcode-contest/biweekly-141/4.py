class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 10**9+7
        dp = [[0 for _ in range(x+1)] for _ in range(n)]
        dp[0][1] = x
        for i in range(1, n):
            for j in range(1, x+1):
                dp[i][j] = dp[i-1][j] * j + dp[i-1][j-1] * (x - j + 1)
                dp[i][j] %= MOD
        ret = 0
        for j in range(1, x+1):
            ret += dp[n-1][j] * pow(y, j, MOD)
            ret %= MOD
        return ret