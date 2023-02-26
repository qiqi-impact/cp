class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        d = defaultdict(int)
        d[0, 0] = 0
        h = [(0, 0, 0)]
        while h:
            c, x, y = heapq.heappop(h)
            
            if d[x, y] != c:
                continue
            
            for dx, dy in pairwise([1, 0, -1, 0, 1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in d:
                    nc = max(c+1, grid[nx][ny])
                    if nc%2 != (nx+ny)%2:
                        nc += 1
                    if (nx, ny) == (R-1, C-1):
                        return nc
                    d[nx, ny] = nc
                    heapq.heappush(h, (nc, nx, ny))
        return -1