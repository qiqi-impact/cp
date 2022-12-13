class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        @cache
        def dp(i, j):
            if i == R:
                return 0
            r = 1e9
            for c in range(j-1, j+2):
                if 0 <= c < C:
                    r = min(r, dp(i+1, c))
            return r + matrix[i][j]
        return min(dp(0, j) for j in range(C))