class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def twoisland():
            seen = set()
            
            def dfs(i, j):
                seen.add((i, j))
                for dx, dy in pairwise([-1, 0, 1, 0, -1]):
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in seen and grid[nx][ny] == 1:
                        dfs(nx, ny)
            
            found = False
            for i in range(R):
                for j in range(C):
                    if (i, j) not in seen and grid[i][j]:
                        if found:
                            return True
                        found = True
                        dfs(i, j)
            return not found
                        
        if twoisland():
            return 0
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if twoisland():
                        return 1
                    grid[i][j] = 1
                    
        return 2