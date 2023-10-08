class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        r = [0] * n
        tot = 0
        for i in range(n):
            if s1[i] != s2[i]:
                r[i] = 1
                tot += 1
        if tot%2: return -1
        
        @cache
        def dp(idx, val):
            if idx == n:
                return 0
            if val is None:
                val = r[idx]
            if idx == n-1:
                return val * (x/2)
            if val == 0:
                return dp(idx+1, None)
            ret = (x/2) + dp(idx+1, None)
            ret = min(ret, 1 + dp(idx+1, 1-r[idx+1]))
            return ret
        
        return int(dp(0, None))