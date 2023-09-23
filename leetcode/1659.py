class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        opts = []
        for i in range(3**n):
            ii = i
            l = []
            for j in range(n):
                l.append(ii%3)
                ii //= 3
            opts.append(tuple(l))

        d = {}
        for x in opts:
            d[x] = {}
            for y in opts:
                sc = 0
                for j in range(n):
                    if y[j] == 1:
                        sc += 120
                        if x[j] == 1:
                            sc -= 60
                        if x[j] == 2:
                            sc -= 10
                        if j > 0 and y[j-1] != 0:
                            sc -= 30
                        if j < n-1 and y[j+1] != 0:
                            sc -= 30
                    elif y[j] == 2:
                        sc += 40
                        if x[j] == 1:
                            sc -= 10
                        if x[j] == 2:
                            sc += 40
                        if j > 0 and y[j-1] != 0:
                            sc += 20
                        if j < n-1 and y[j+1] != 0:
                            sc += 20
                d[x][y] = sc

        @cache
        def dp(idx, last, li, le):
            if idx == m:
                return 0
            ret = -inf
            for x in opts:
                i = x.count(1)
                e = x.count(2)
                if i <= li and e <= le:
                    ret = max(ret, d[last][x] + dp(idx+1, x, li-i, le-e))
            return ret

        return dp(0, tuple([0] * n), introvertsCount, extrovertsCount)