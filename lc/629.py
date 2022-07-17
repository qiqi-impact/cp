class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9+7
        ret = [0] * (k+1)
        ret[0] = 1
        for i in range(n-1):
            p = [0]
            for j in range(len(ret)):
                p.append(p[-1] + ret[j])
            for t in range(len(ret)-1, -1, -1):
                s = p[t+1]
                if t+1-(i+2) >= 0:
                    s -= p[t+1-(i+2)]
                ret[t] = s % MOD
        return ret[k]