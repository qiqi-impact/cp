class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        lh = [[int(x) for x in str(low-1)], [int(x) for x in str(high)]]

        @cache
        def dp(idx, df, w, lmt):
            if idx == len(lh[w]):
                return int(df == 0)
            ed = 9
            if lmt:
                ed = lh[w][idx]
            ret = 0
            m = 1 if idx % 2 else -1
            for d in range(0, ed+1):
                nlmt = lmt
                if d != ed:
                    nlmt = False
                ret += dp(idx+1, df + m * d, w, nlmt)
            return ret

        return dp(0, 0, 1, True) - dp(0, 0, 0, True)