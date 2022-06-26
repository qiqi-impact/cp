class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if i == j or i+j == R-1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True