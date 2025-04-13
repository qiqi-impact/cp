MOD = 10**9+7

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
    
class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        l = numberToBase(int(l)-1, b)
        r = numberToBase(int(r), b)
        A = [l, r]
        
        @cache
        def dp(idx, lr, lim, st):
            if idx == -1:
                return 1
            arr = A[lr]
            ret = 0
            for i in range(st, b if not lim else arr[-idx-1]+1):
                nl = lim
                if lim and i != arr[-idx-1]:
                    nl = False
                ret += dp(idx-1, lr, nl, i)
                ret %= MOD
            return ret
        
        x = 0
        for i in range(len(l)):
            x += dp(i, 0, i == len(l)-1, 1)

        y = 0
        for i in range(len(r)):
            y += dp(i, 1, i == len(r)-1, 1)

        dp.cache_clear()

        ret = y - x
        return ret % MOD
            
        ©leetcode