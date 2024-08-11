class Solution:
    def countOfPairs(self, a: List[int]) -> int:
        n = len(a)
        MX = max(a)
        dp = [[0 for _ in range(MX+1)] for _ in range(2)]
        ps = [[0 for _ in range(MX+2)] for _ in range(2)]
        MOD = 10**9+7

        for i in range(a[n-1]+1):
            dp[(n-1)%2][i] = 1
            ps[(n-1)%2][i+1] = ps[(n-1)%2][i] + dp[(n-1)%2][i]
            
        for i in range(n-2, -1, -1):
            for j in range(MX+1):
                l = j + max(a[i+1] - a[i], 0)
                r = a[i+1]
                if l <= r:
                    dp[i%2][j] = (ps[(i+1)%2][r+1] - ps[(i+1)%2][l])%MOD
                else:
                    dp[i%2][j] = 0
                ps[i%2][j+1] = (ps[i%2][j] + dp[i%2][j])%MOD
        return ps[0][-1] % MOD