class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        @cache
        def dp(i, j, z):
            if z == 0:
                return 0
            ret = 0
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = i+dx, j+dy
                if nx == -1 or nx == m or ny == -1 or ny == n:
                    ret += 1
                else:
                    ret += dp(nx, ny, z-1)
            return ret%MOD
        return dp(startRow, startColumn, maxMove)