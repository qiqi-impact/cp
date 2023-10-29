class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        @cache
        def dp(p, t):
            if p == 0 or t == 0:
                return 1
            ret = 0
            for i in range(p+1):
                ret += math.comb(p, i) * dp(p-i, t-1)
            return ret

        i = 0
        while 1:
            if dp(i, minutesToTest//minutesToDie) >= buckets:
                return i
            i += 1