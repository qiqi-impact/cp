from collections import deque

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dist = [[[inf,inf] for _ in range(C)] for _ in range(R)]
        q = deque([(0, 0)])
        dist[0][0][0] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0 and dist[nx][ny][0] == inf:
                    dist[nx][ny][0] = dist[x][y][0] + 1
                    q.append((nx, ny))
        
        q = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j][1] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0 and dist[nx][ny][1] == inf:
                    dist[nx][ny][1] = dist[x][y][1] + 1
                    q.append((nx, ny))

        def can(k):
            q = deque([(0, 0)])
            seen = set(q)
            while q:
                x, y = q.popleft()
                for dx, dy in pairwise([1,0,-1,0,1]):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0 and dist[nx][ny][0] + k - int((nx,ny)==(R-1,C-1)) < dist[nx][ny][1] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))
                        if (nx, ny) == (R-1, C-1):
                            return True

        if not can(0):
            return -1

        l, r = 0, 10**9
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l