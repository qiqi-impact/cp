class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        pw = [20]
        for i in range(100):
            pw.append(pw[-1] * pw[-1] % MOD)
        
        k = n//2
        ret = 1
        for i in range(100):
            if k & (1 << i):
                ret *= pw[i]
                ret %= MOD
        
        return ret * pow(5, n%2) % MOD