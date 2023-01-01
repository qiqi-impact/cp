class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append((0, i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        while q:
            c, i, j = q.popleft()
            for dx, dy in pairwise([1, 0, -1, 0, 1]):
                nx, ny = i+dx, j+dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((c+1, nx, ny))
                    if fresh == 0:
                        return c+1
        return -1