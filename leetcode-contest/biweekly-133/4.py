class Solution:
    def numberOfPermutations(self, n: int, r: List[List[int]]) -> int:
        MOD = 10**9+7
        mx = n * (n - 1) // 2
        d = {}
        for x, y in r:
            d[x] = y
            if x == 0 and y != 0:
                return 0
        dp = [[0 for _ in range(mx+1)] for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, n):
            t = 0
            for j in range(i*(i+1)//2+1):
                t += dp[i-1][j]
                t %= MOD
                if j >= i+1:
                    t -= dp[i-1][j-i-1]
                    t %= MOD
                if i not in d or j == d[i]:
                    dp[i][j] = t
        return sum(dp[n-1]) % MOD