class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        if d > len(jd):
            return -1
        @cache
        def dp(idx, days):
            if days == 1:
                mx = 0
                for i in range(idx, len(jd)):
                    mx = max(mx, jd[i])
                return mx
            ret = 1e18
            mx = 0
            for i in range(idx, len(jd) - days + 1):
                mx = max(mx, jd[i])
                ret = min(ret, mx + dp(i+1, days-1))
            return ret
        return dp(0, d)