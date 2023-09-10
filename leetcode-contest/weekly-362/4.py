class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MOD = 10**9+7
        
        h = 0
        for c in s:
            h = (26 * h + (ord(c)-97)) % MOD
            
        th = 0
        for c in t:
            th = (26 * th + (ord(c)-97)) % MOD
            
        x = 0
        df = h == th
        if df:
            x += 1
        n = len(s)
        
        q = pow(26, n-1, MOD)
        
        for i in range(1, n):
            h = ((h - q * (ord(s[i-1])-97)) * 26 + (ord(s[(i+n-1)%n])-97))%MOD
            if h == th:
                x += 1
        
        ret = ((pow(n-1, k, MOD) - pow(-1, k, MOD)) * pow(n, -1, MOD) * x % MOD)
        
        if df:
            ret += (-1 if k%2 else 1)
            ret %= MOD
        return ret