class Solution:
    def minChanges(self, s: str) -> int:
        l = [int(c) for c in s]
        @cache
        def dp(idx, c, ln):
            if idx == len(s):
                return 0
            ret = inf
            for x in [0, 1]:
                df = int(x != l[idx])
                if x == c:
                    ret = min(ret, df + dp(idx+1, x, (ln+1)%2))
                else:
                    if not ln%2:
                        ret = min(ret, df + dp(idx+1, x, 1))
            return ret
        return dp(0, None, 0)