class Solution:
    def solve(self, m):
        
        R, C = len(m), len(m[0])
        cost = [[float('inf') for _ in range(C)] for _ in range(R)]
        cost[0][0] = 0

        h = [(0, 0, 0)]
        mx = 0
        while h:
            c, i, j = heappop(h)
            if c != cost[i][j]:
                continue
            for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                ni, nj = i+di, j+dj
                
                if 0 <= ni < R and 0 <= nj < C:
                    nc = c
                    if m[i][j] != m[ni][nj]:
                        nc += 1
                    if cost[ni][nj] > nc:
                        cost[ni][nj] = nc
                        mx = max(mx, nc)
                        heappush(h, (nc, ni, nj))
        return mx