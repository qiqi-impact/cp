class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = 0
            ret = 1
            for dx, dy in pairwise([-1, 0, 1, 0, -1]):
                nx, ny = i+dx, j+dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny]:
                    ret += dfs(nx, ny)
            return ret
        mx = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    mx = max(mx, dfs(i, j))
        return mx