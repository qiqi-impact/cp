class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        sm = [[0 for _ in range(C)] for _ in range(R)]
        ct = 0
        for i in range(R):
            for j in range(C):
                q = grid[i][j]
                if i > 0:
                    q += sm[i-1][j]
                if j > 0:
                    q += sm[i][j-1]
                if i > 0 and j > 0:
                    q -= sm[i-1][j-1]
                sm[i][j] = q
                if q <= k:
                    ct += 1
        return ct