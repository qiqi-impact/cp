class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = int(1e9)+7
        R, C = len(grid), len(grid[0])
        m = [[[0 for _ in range(k)] for _ in range(C)] for _ in range(R)]
        m[0][0][grid[0][0]%k] = 1
        for i in range(R):
            for j in range(C):
                if i+j == 0: continue
                v = grid[i][j]
                if j > 0:
                    for t in range(k):
                        m[i][j][(t+v)%k] += m[i][j-1][t]
                        m[i][j][(t+v)%k] %= MOD
                if i > 0:
                    for t in range(k):
                        m[i][j][(t+v)%k] += m[i-1][j][t]
                        m[i][j][(t+v)%k] %= MOD
        return m[R-1][C-1][0]