from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        def bfs(x, y):
            q = deque([(x, y)])
            grid[x][y] = '0'
            while q:
                x, y = q.popleft()
                for dx, dy in [[-1,0], [1, 0], [0,-1], [0, 1]]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        q.append((nx, ny))
        ret = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    ret += 1
                    bfs(i, j)
        return ret