class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        D = [[-1,0],[1,0],[0,1],[0,-1]]
        
        dp = {(0,0):0}
        h = [(0,0,0)]
        while h:
            m,x,y = heapq.heappop(h)
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C:
                    nm = m + int(grid[nx][ny])
                    if dp.get((nx, ny), 1e9) > nm:
                        dp[nx,ny] = nm
                        heapq.heappush(h, (nm,nx,ny))
                    if (nx,ny) == (R-1, C-1):
                        return dp[nx,ny]