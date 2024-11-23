class Solution:
    def maxCollectedFruits(self, g: List[List[int]]) -> int:
        n = len(g)
        a = 0
        for i in range(n):
            a += g[i][i]
            g[i][i] = 0

        @cache
        def dp1(i, j):
            if i >= n:
                return -inf
            cur = g[i][j]
            if (i, j) == (n-1, n-1):
                return cur
            ret = -inf
            for k in range(j-1, j+2):
                if 0 <= k < n:
                    ret = max(ret, dp1(i+1, k))
            return cur + ret

        @cache
        def dp2(i, j):
            if j >= n:
                return -inf
            cur = g[i][j]
            if (i, j) == (n-1, n-1):
                return cur
            ret = -inf
            for k in range(i-1, i+2):
                if 0 <= k < n:
                    ret = max(ret, dp2(k, j+1))
            return cur + ret

        return a + dp1(0, n-1) + dp2(n-1, 0)