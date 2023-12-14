class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        tr, tc = [0]*R, [0]*C
        for i in range(R):
            for j in range(C):
                tr[i] += grid[i][j]
                tc[j] += grid[i][j]
        ret = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                ret[i][j] = tr[i] + tc[j] - (R - tr[i]) - (C - tc[j])
        return ret