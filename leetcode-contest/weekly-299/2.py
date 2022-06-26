class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9+7
        d = {
            0: [0, 1, 2, 3],
            1: [0, 2],
            2: [0, 1],
            3: [0],
        }
        @cache
        def dp(idx, last):
            if idx == n:
                return 1
            ret = 0
            for x in d[last]:
                ret += dp(idx+1, x)
            ret %= MOD
            return ret
        return dp(0, 0)