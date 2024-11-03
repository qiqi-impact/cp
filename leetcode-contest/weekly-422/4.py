MOD = 10**9+7

@cache
def comb(x, y):
    if y == 0 or y == x:
        return 1
    return (comb(x-1, y-1) + comb(x-1, y)) % MOD

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        SM = 0
        l = [0] * 10
        tot = [0] * 10
        tc = [0] * 10
        for x in num:
            l[int(x)] += 1
            SM += int(x)
        if SM % 2:
            return 0
        
        @cache
        def dp(idx, ct, sm):
            if idx == -1:
                return int(ct == 0 and sm == 0)
            ct2 = tc[idx] - ct
            sm2 = tot[idx] - sm
            ret = 0
            for t in range(l[idx] + 1):
                if t > ct or l[idx] - t > ct2 or idx * t > sm or idx * (l[idx] - t) > sm2:
                    continue
                v = dp(idx-1, ct - t, sm - (idx) * t)
                ret += comb(ct, t) * comb(ct2, l[idx] - t) * v % MOD
                ret %= MOD
            return ret

        return dp(9, (len(num)+1)//2, SM//2)