MOD = 10**9+7

class Solution:
    def numTilings(self, n: int) -> int:
        
        @cache
        def f(t, b):
            if t < b:
                return f(b, t)
            if t == b:
                if b <= 1:
                    return 1
                return (f(t-2, b-2) + f(t-1, b-1) + 2 * f(t-1, b-2)) % MOD
            else:
                if b == 0:
                    return 0
                return (f(b, t-2) + f(t-2, b-1)) % MOD
            
        return f(n, n)