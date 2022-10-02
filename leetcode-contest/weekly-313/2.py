class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        mx = -1e18
        R, C = len(grid), len(grid[0])
        for i in range(1, R-1):
            for j in range(1, C-1):
                s = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx != 0 or dy == 0:
                            s += grid[i+dx][j+dy]
                mx = max(mx, s)
        return mx