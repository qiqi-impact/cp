class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        pf = [-1] * n
        sf = [-1] * n
        for i in range(n):
            if forts[i] == 1:
                pf[i] = i
            elif i > 0:
                pf[i] = pf[i-1]
                if forts[i-1] == -1:
                    pf[i] = -1
        for i in range(n-1, -1, -1):
            if forts[i] == 1:
                sf[i] = i
            elif i < n-1:
                sf[i] = sf[i+1]
                if forts[i+1] == -1:
                    sf[i] = -1
        ret = 0
        for i in range(n):
            if forts[i] == -1:
                if pf[i] != -1:
                    ret = max(ret, i - pf[i] - 1)
                if sf[i] != -1:
                    ret = max(ret, sf[i] - i - 1)
        return ret