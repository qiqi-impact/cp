class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        omzr, omzc = [0 for _ in range(R)], [0 for _ in range(C)]
        for i in range(R):
            for j in range(C):
                omzr[i] += (1 if grid[i][j] else -1)
                omzc[j] += (1 if grid[i][j] else -1)
        ret = [[None for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                ret[i][j] = omzr[i] + omzc[j]
        return ret