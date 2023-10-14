class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 10**9+7
        ct = Counter(nums)
        def f(x):
            if x < 0:
                return 0
            dp = [0] * (x+1)
            dp[0] = 1
            for k in ct:
                if k == 0:
                    for i in range(x+1):
                        dp[i] *= (ct[k]+1)
                        dp[i] %= MOD
                else:
                    md = [0] * k
                    q = [0] * (x+1)
                    for i in range(x+1):
                        md[i%k] += dp[i]
                        q[i] = md[i%k]
                    for i in range(x+1):
                        dp[i] = q[i]
                        v = i-k*(ct[k]+1)
                        if v >= 0:
                            dp[i] -= q[v]
                        dp[i] %= MOD
                    print(k, md, q)
            return sum(dp) % MOD
        
        return (f(r) - f(l-1)) % MOD