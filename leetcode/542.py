from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        q = deque()
        dist = [[1e9 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dx, dy in pairwise([1, 0, -1, 0, 1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and dist[nx][ny] > 1 + dist[x][y]:
                    dist[nx][ny] = 1 + dist[x][y]
                    q.append((nx, ny))
        return dist