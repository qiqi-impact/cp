class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        row = [0] * R
        col = [0] * C
        tot = 0
        for i in range(R):
            for j in range(C):
                tot += grid[i][j]
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        prow = [0]
        for i in range(R):
            prow.append(prow[-1] + row[i])
            if i != R - 1 and prow[-1] * 2 == tot:
                return True
        pcol = [0]
        for i in range(C):
            pcol.append(pcol[-1] + col[i])
            if i != C - 1 and pcol[-1] * 2 == tot:
                return True
        return False
                