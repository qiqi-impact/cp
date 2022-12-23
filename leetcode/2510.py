class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        dp = [[set() for _ in range(C)] for _ in range(R)]
        
        dp[0][0].add(1 if grid[0][0] == 1 else -1)
        for i in range(R):
            for j in range(C):
                if i + j == 0:
                    continue
                v = 1 if grid[i][j] == 1 else -1
                dp[i][j] = set()
                if j > 0:
                    dp[i][j] = dp[i][j] | {x+v for x in dp[i][j-1]}
                if i > 0:
                    dp[i][j] = dp[i][j] | {x+v for x in dp[i-1][j]}
        return 0 in dp[-1][-1]