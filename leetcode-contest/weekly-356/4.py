class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9+7
        a = [low, high]
        
        @cache
        def dp(dig, prv, lim):
            if dig == 0:
                return 1
            cap = 9
            if lim < 2:
                cap = int(a[lim][-dig])
            ret = 0
            if prv == -1:
                for i in range(1, cap+1):
                    if i == cap:
                        ret += dp(dig-1, i, lim)
                    else:
                        ret += dp(dig-1, i, 2)
            else:
                for x in [prv-1, prv+1]:
                    if 0 <= x <= min(cap, 9):
                        ret += dp(dig-1, x, lim if x==cap else 2)
            return ret % MOD
        
        ans = 0
        for i in range(1, len(low)):
            ans -= dp(i, -1, 2)
        ans -= dp(len(low), -1, 0)
        
        for i in range(1, len(high)):
            ans += dp(i, -1, 2)
        ans += dp(len(high), -1, 1)
        
        fail = False
        for i, c in enumerate(low):
            if i > 0:
                if abs(int(low[i-1]) - int(low[i])) != 1:
                    fail = True
                    break
        if not fail:
            ans += 1
        
        return ans % MOD
        
        