class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        mm = [[0 for _ in range(C)] for _ in range(R)]
        for j in range(C-2, -1, -1):
            for i in range(R):
                for nr in [i-1, i, i+1]:
                    if 0 <= nr < R and grid[nr][j+1] > grid[i][j]:
                        mm[i][j] = max(mm[i][j], 1 + mm[nr][j+1])
        return max([mm[i][0] for i in range(R)])