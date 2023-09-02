MX = 10**5+1
MOD = 10**9+7

FAC = [1]
for i in range(1, MX):
    FAC.append(FAC[-1] * i % MOD)
    
def p(y, k):
    return (FAC[y] * pow(FAC[k], -1, MOD) * pow(FAC[y-k], -1, MOD)) % MOD

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        f = Counter(s)
        ct = {}
        for x in f:
            ct[f[x]] = ct.get(f[x], 0) + 1
        l = list(ct.items())
        l.sort(reverse=True)
        
        ret = 1
        for i in range(len(l)):
            x, y = l[i]
            if k >= y:
                k -= y
                ret *= pow(x, y, MOD)
                ret %= MOD
            else:
                ret *= p(y, k) * pow(x, k, MOD)
                ret %= MOD
                k = 0
        return ret if k == 0 else 0