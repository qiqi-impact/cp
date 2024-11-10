class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9+7
        
        @cache
        def dist(x):
            if x == 0:
                return inf
            if x == 1:
                return 0
            t = x.bit_count()
            return 1 + dist(t)

        @cache
        def ct(idx, limit, amt):
            if idx == len(s):
                return int(dist(amt) <= k - 1)
            if not limit:
                return (ct(idx+1, False, amt+1) + ct(idx+1, False, amt)) % MOD
            else:
                if idx == len(s) - 1:
                    if s[idx] == '1':
                        return (ct(idx+1, False, amt)) % MOD
                    else:
                        return 0
                else:
                    if s[idx] == '1':
                        return (ct(idx+1, True, amt+1) + ct(idx+1, False, amt)) % MOD
                    else:
                        return ct(idx+1, True, amt)

        return ct(0, True, 0) % MOD
        