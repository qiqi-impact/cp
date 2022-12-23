class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        if (R+C-1)%2:
            return False
        dp = [[None for _ in range(C)] for _ in range(R)]
        
        dp[0][0] = [grid[0][0], grid[0][0]]
        for i in range(R):
            for j in range(C):
                if i + j == 0:
                    continue
                v = 1 if grid[i][j] == 1 else -1
                if i == 0:
                    dp[i][j] = [dp[i][j-1][0] + v, dp[i][j-1][1] + v]
                elif j == 0:
                    dp[i][j] = [dp[i-1][j][0] + v, dp[i-1][j][1] + v]
                else:
                    dp[i][j] = [min(dp[i-1][j][0], dp[i][j-1][0]) + v, max(dp[i-1][j][1], dp[i][j-1][1]) + v]
        return dp[-1][-1][0] <= 0 <= dp[-1][-1][1]