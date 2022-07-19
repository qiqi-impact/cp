class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(C)] for _ in range(R)]
        dp[0][0] = grid[0][0]
        for i in range(R):
            for j in range(C):
                if i+j == 0:
                    continue
                dp[i][j] = float('inf')
                if i > 0: dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0: dp[i][j] = min(dp[i][j], dp[i][j-1])
                dp[i][j] += grid[i][j]
        return dp[-1][-1]