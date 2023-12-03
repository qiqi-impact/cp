MOD = 10**9+7
fac = [1]
inv = [None]
pw2 = [1]
for i in range(1, 10**5):
    fac.append((fac[-1] * i)%MOD)
    inv.append(pow(fac[-1], -1, MOD))
    pw2.append(pw2[-1] * 2 % MOD)

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        ret = 1
        gaps = []
        sg = 0
        pw = 0
        sick.sort()
        # ss = set(sick)
        if sick[0] != 0:
            gaps.append(sick[0])
        if sick[-1] != n-1:
            gaps.append(n-1 - sick[-1])
        for i in range(1, len(sick)):
            if sick[i] - sick[i-1] > 1:
                gaps.append(sick[i] - sick[i-1] - 1)
                pw += sick[i] - sick[i-1] - 2
        
        if not gaps:
            return 1
        
        ret *= fac[sum(gaps)]
        for x in gaps:
            ret *= inv[x]
            ret %= MOD
        ret *= pw2[pw]
        return ret%MOD
        
                
                
        