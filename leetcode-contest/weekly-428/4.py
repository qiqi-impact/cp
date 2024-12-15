class Solution:
    def makeStringGood(self, s: str) -> int:
        f = [0] * 26
        for c in s:
            f[ord(c)-97] += 1
        ret = len(s)
        m = max(f)
        for i in range(1, m+1):
            d = [0, 0]
            for j in range(26):
                p = 0
                if j > 0:
                    if f[j-1] >= i:
                        p = f[j-1] - i
                    else:
                        p = f[j-1]
                if f[j] == i:
                    continue
                if f[j] > i:
                    a1 = inf
                    a2 = inf
                    b = f[j] - i
                else:
                    a1 = max(0, (i - f[j]) - p)
                    a2 = i - f[j]
                    b = f[j]

                x = min(d[1] + a1, d[0] + a2)
                y = min(d) + b
                d = [x, y]
            ret = min(ret, min(d))
        return ret