class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        x = abs(s-e)
        if x > k:
            return 0
        if x%2 != k%2:
            return 0
        comb = [[0 for _ in range(k+1)] for _ in range(k+1)]
        comb[0][0] = 1
        for i in range(1, k+1):
            for j in range(0, i+1):
                comb[i][j] += comb[i-1][j]
                if j > 0:
                    comb[i][j] += comb[i-1][j-1]
                comb[i][j] %= (10**9+7)
        # print(comb)
        return comb[k][(k-x)//2]