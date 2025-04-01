class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def ff(x, y):
            dist = [[inf for _ in range(C)] for _ in range(R)]
            dist[x][y] = 0
            q = deque([(x, y)])
            while q:
                a, b = q.popleft()
                for dx, dy in pairwise([1,0,-1,0,1]):
                    nx, ny = a+dx, b+dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 0 and dist[nx][ny] == inf:
                        dist[nx][ny] = dist[a][b] + 1
                        q.append((nx, ny))
            return dist
        ret = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    t = ff(i, j)
                    for k in range(R):
                        for l in range(C):
                            ret[k][l] += t[k][l]
        mn = inf
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    mn = min(mn, ret[i][j])
        return mn if mn != inf else -1