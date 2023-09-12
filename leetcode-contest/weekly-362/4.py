class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 10**9+7

        x = 0
        df = False
        if s == t:
            x += 1
            df = True

        ss = s+s
        n = len(s)
        idx = ss.find(t, 1)
        if idx != n and idx != -1:
            x += 1
            i2 = ss.find(t, idx+1)
            if i2 != n and i2 != -1:
                per = i2 - idx
                x += (n - 1 - idx) // per
        
        ret = ((pow(n-1, k, MOD) - pow(-1, k, MOD)) * pow(n, -1, MOD) * x % MOD)
        
        if df:
            ret += (-1 if k%2 else 1)
            ret %= MOD
        return ret