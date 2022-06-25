class Solution:
    def distinctSequences(self, n: int) -> int:
        @cache
        def dp(idx, p1, p2):
            if idx == n:
                return 1
            ret = 0
            for i in range(1, 7):
                if i != p1 and i != p2 and (idx == 0 or math.gcd(p2, i) == 1):
                    ret += dp(idx+1, p2, i)
            ret %= (int(1e9)+7)
            return ret
        return dp(0,0,0)