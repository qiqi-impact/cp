from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        def fill(init):
            vis = set(init)
            q = deque(init)
            while q:
                x, y = q.popleft()
                for dx, dy in [[-1,0], [1,0], [0,-1], [0,1]]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C and heights[nx][ny] >= heights[x][y] and (nx, ny) not in vis:
                        vis.add((nx, ny))
                        q.append((nx, ny))
            return vis
        pacific, atlantic = [], []
        for i in range(R):
            for j in range(C):
                if i == 0 or j == 0:
                    pacific.append((i, j))
                if i == R-1 or j == C-1:
                    atlantic.append((i, j))
        return list(fill(pacific) & fill(atlantic))