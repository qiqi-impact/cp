class Solution:
    def maxRemovals(self, s: str, p: str, t: List[int]) -> int:
        t = set(t)
        @cache
        def dp(si, pi):
            if si == len(s):
                return -inf if pi != len(p) else 0
            if pi == len(p):
                return int(si in t) + dp(si+1, pi)
            ret = int(si in t) + dp(si+1, pi)
            if s[si] == p[pi]:
                ret = max(ret, dp(si+1, pi+1))
            return ret
        r = dp(0, 0)
        dp.cache_clear()
        return r