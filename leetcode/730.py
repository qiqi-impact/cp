class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9+7
        d = [[] for _ in range(4)]
        for i, x in enumerate(s):
            d[ord(x)-97].append(i)
        
        @cache
        def f(l, r):
            ret = 0
            for c in range(4):
                a = bisect.bisect_left(d[c], l)
                b = bisect.bisect_left(d[c], r+1) - 1
                if a > b:
                    continue
                ret += min(2, b-a+1)
                ret += f(d[c][a]+1, d[c][b]-1)
                ret %= MOD
            return ret

        return f(0, len(s)-1)