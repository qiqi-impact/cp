class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = int(1e9)+7
        @cache
        def dp(idx):
            if idx == 0:
                return 1
            ret = 0
            if idx >= zero:
                ret += dp(idx - zero) 
            if idx >= one:
                ret += dp(idx - one) 
            ret %= MOD
            return ret
        ret = 0
        for i in range(low, high+1):
            ret += dp(i)
            ret %= MOD
        return ret