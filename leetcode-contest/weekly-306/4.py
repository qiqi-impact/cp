class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        @cache
        def dfs(t, lz, used):
            if not t:
                return 1
            ret = 0
            rng = range(int(not lz), t[0]+1)
            for c in rng:
                if used & (1 << c) == 0:
                    rem = t[1:] if c == t[0] else tuple([9] * (len(t)-1))
                    ret += dfs(rem, lz or c != 0, used ^ (1 << c))
            return ret
        
        digits = [int(c) for c in str(n)]
        f = 0
        for i in range(1, len(digits)):
            f += dfs(tuple([9] * i), False, 0)
        return f + dfs(tuple(digits), False, 0)