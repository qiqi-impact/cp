class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(a, b):
            if b < 0 or a < 0:
                return 0
            if b == 0:
                if a == 0:
                    return 1
                if a == 1:
                    return 0
            if a-2 == b:
                ret = dp(a-2, b)%MOD
            if a-1 == b:
                ret = (dp(a-2, b-1) + dp(b, a-2))%MOD
            if a == b:
                ret = (dp(a-1, b-1) + dp(a, b-2) + 2 * dp(a-1, b-2))%MOD
            return ret
        return dp(n, n)