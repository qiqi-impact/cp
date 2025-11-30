class Solution:
    def countDistinct(self, n: int) -> int:
        s = [int(c) for c in str(n)]
        
        @cache
        def dp(idx, limit, st):
            if idx == len(s):
                return 1
            q = s[idx]
            if not limit:
                q = 9
            ret = 0
            r = 0
            if st:
                r = 1
            for dig in range(r, q + 1):
                nl = limit
                if dig < q:
                    nl = False
                nst = st
                if dig >= 1:
                    nst = True
                ret += dp(idx + 1, nl, nst)
            # print(idx, limit, st, ret)
            return ret

        return dp(0, True, False) - 1
                