class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(idx):
            if idx == len(s):
                return 1
            cur = 0
            ret = 0
            for x in range(idx, len(s)):
                cur = 10 * cur + int(s[x])
                if 1 <= cur <= 26:
                    ret += dp(x+1)
                else:
                    break
            return ret
        return dp(0)