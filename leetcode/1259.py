class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        @cache
        def dp(x):
            if x == 0:
                return 1
            ret = 0
            for i in range(0, x, 2):
                ret += dp(i) * dp(x-2-i)
                ret %= 10**9+7
            return ret
        return dp(numPeople)