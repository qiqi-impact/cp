class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def dp(i, j, p):
            if i > j:
                return 0
            if s[i] == p:
                return dp(i+1, j, p)
            ret = 1 + dp(i+1, j, p)
            for k in range(i+1, j+1):
                if s[k] == s[i]:
                    ret = min(ret, 1 + dp(i+1, k-1, s[i]) + dp(k+1, j, p))
            return ret
        return dp(0, len(s)-1, None)