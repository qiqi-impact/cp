class Solution:
    def countPalindromes(self, s: str) -> int:
        n = len(s)
        idxs = [[] for _ in range(10)]
        for i, c in enumerate(s):
            c = int(c)
            idxs[c].append(i)
        dfl = [[0 for _ in range(10)] for _ in range(n)]
        for i in range(n):
            if i > 0:
                for j in range(10):
                    dfl[i][j] = dfl[i-1][j]
            dfl[i][int(s[i])] += 1
        dfr = [[0 for _ in range(10)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            if i < n - 1:
                for j in range(10):
                    dfr[i][j] = dfr[i+1][j]
            dfr[i][int(s[i])] += 1
        # print(dfr)
        ret = 0
        for dig in range(10):
            l = idxs[dig]
            rp = len(l)
            cum = [0] * 10
            ct = [0] * 10
            # print(l)
            for lp in range(len(l)-1, -1, -1):
                while l[rp-1] > l[lp] + 1:
                    rp -= 1
                    for j in range(10):
                        cum[j] += dfr[l[rp]][j] * (l[rp] - 1)
                        ct[j] += dfr[l[rp]][j]
                        if j == dig:
                            cum[j] -= (l[rp] - 1)
                            ct[j] -= 1
                # print(cum)
                # print(ct)
                for j in range(10):
                    v = dfl[l[lp]][j]
                    if dig == j:
                        v -= 1
                    ret += v * (cum[j] - ct[j] * l[lp])
                    ret %= int(10**9+7)
                # print(ret)
        return ret
                        