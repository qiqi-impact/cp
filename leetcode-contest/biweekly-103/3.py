class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        cur = 0
        def dfs(i, j):
            nonlocal cur
            cur += grid[i][j]
            grid[i][j] = 0
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = i+dx, j+dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != 0:
                    dfs(nx, ny)
        
        mx = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    cur = 0
                    dfs(i, j)
                    mx = max(cur, mx)
        return mx