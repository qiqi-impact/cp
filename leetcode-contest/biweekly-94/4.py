class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10**9+7
        
        fac = [1]
        for i in range(1, 10**5+1):
            fac.append(fac[-1]*i%MOD)
        
        l = s.split(' ')
        ret = 1
        for w in l:
            ct = Counter(w)
            v = list(ct.values())
            sv = sum(v)
            ret *= fac[sv]
            ret %= MOD
            for q in v:
                ret *= pow(fac[q], -1, MOD)
                ret %= MOD
        return ret