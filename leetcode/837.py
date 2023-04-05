class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n == 0 or k == 0:
            return 1
        pf = [0, 1]
        for i in range(1, k):
            cur = (pf[i] - pf[max(0, i-maxPts)])/maxPts
            pf.append(pf[-1] + cur)
        ret = 0
        for i in range(k, min(k+maxPts, n+1)):
            cur = (pf[k] - pf[max(0, i-maxPts)])/maxPts
            ret += cur
        return ret