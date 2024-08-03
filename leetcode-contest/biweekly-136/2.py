class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = 0
        for i in range(R):
            for j in range(C//2):
                if grid[i][j] != grid[i][C-1-j]:
                    q += 1
        t = 0
        for j in range(C):
            for i in range(R//2):
                if grid[i][j] != grid[R-1-i][j]:
                    t += 1
        return min(q,t)