class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        @cache
        def dp(i, j):
            ret = inf
            for k in range(C):
                v = grid[i][j]
                if i > 0:
                    v += dp(i-1, k) + moveCost[grid[i-1][k]][j]
                ret = min(ret, v)
            return ret
        return min([dp(R-1, j) for j in range(C)])