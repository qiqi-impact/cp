class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        dist = [[[1e9, 1e9] for _ in range(c)] for _ in range(r)]
        
        D = [[-1,0], [1,0], [0,-1], [0,1]]
        
        q = [(0,0)]
        qp = 0
        dist[0][0][0] = 0
        while qp < len(q):
            x,y = q[qp]
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != 2 and dist[nx][ny][0] > dist[x][y][0] + 1:
                    dist[nx][ny][0] = dist[x][y][0] + 1
                    q.append((nx, ny))
            qp += 1
            
        q = []
        qp = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j][1] = 0
        while qp < len(q):
            x,y = q[qp]
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != 2 and dist[nx][ny][1] > dist[x][y][1] + 1:
                    dist[nx][ny][1] = dist[x][y][1] + 1
                    q.append((nx, ny))
            qp += 1
            
        def dfs(diff):
            seen = set([(0, 0)])
            q = [(0,0)]
            qp = 0
            while qp < len(q):
                x,y = q[qp]
                for dx, dy in D:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < r and 0 <= ny < c:
                        if dist[nx][ny][1] - dist[nx][ny][0] >= diff and (nx, ny) == (r-1, c-1):
                            return True
                        if dist[nx][ny][1] - dist[nx][ny][0] > diff and (nx, ny) not in seen:
                            q.append((nx, ny))
                            seen.add((nx, ny))
                qp += 1
            return False
        
        if not dfs(0):
            return -1
        if dfs(r*c):
            return int(1e9)
        
        a, b = 0, r*c
        while a < b:
            mi = (a+b+1)//2
            if dfs(mi):
                a = mi
            else:
                b = mi-1
        return a
            
            