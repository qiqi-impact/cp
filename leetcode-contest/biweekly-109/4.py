class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9+7
        pw = []
        for i in range(1, n+1):
            v = i ** x
            if v > n:
                break
            pw.append(v)
        
        @cache
        def dp(idx, left):
            if idx == -1:
                return int(left == 0)
            v = pw[idx]
            ret = dp(idx-1, left)
            if v <= left:
                ret += dp(idx-1, left - v)
                ret %= MOD
            return ret
        
        return dp(len(pw)-1, n)