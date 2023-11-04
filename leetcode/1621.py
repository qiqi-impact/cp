class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        n -= 1
        MOD = 10**9+7
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for kk in range(1, k+1):
            sm = 0
            for i in range(1, n+1):
                sm += dp[i-1][kk-1]
                dp[i][kk] = (dp[i-1][kk] + sm) % MOD
        ret = 0
        for i in range(n+1):
            ret += dp[i][k]
            ret %= MOD
        return ret