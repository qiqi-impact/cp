class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        src = []
        dst = []
        for i in range(3):
            for j in range(3):
                grid[i][j] -= 1
                if grid[i][j] < 0:
                    dst.append((i, j))
                elif grid[i][j] > 0:
                    for _ in range(grid[i][j]):
                        src.append((i, j))
        if not dst:
            return 0
                        
        used = [0] * len(src)
        
        ret = inf
        cur = 0
        def dfs(idx):
            nonlocal cur, ret
            if idx == len(dst):
                ret = min(ret, cur)
                return
            for i in range(len(src)):
                if not used[i]:
                    dx = abs(src[i][0] - dst[idx][0])
                    dy = abs(src[i][1] - dst[idx][1])
                    used[i] = True
                    cur += dx + dy
                    dfs(idx+1)
                    cur -= dx + dy
                    used[i] = False
        dfs(0)
        return ret