class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        dist = {}

        def fill(x, y):
            d = {(x, y): 0}
            q = deque([(x, y)])
            while q:
                cx, cy = q.popleft()
                for dx, dy in [[-2,1], [2,1], [-2,-1], [2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]:
                    nx, ny = cx+dx, cy+dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and (nx, ny) not in d:
                        d[nx, ny] = d[cx, cy] + 1
                        q.append((nx, ny))
            dist[x, y] = d

        for x, y in positions:
            fill(x, y)
        
        fill(kx, ky)

        tot = (1 << len(positions)) - 1

        @cache
        def dp(cx, cy, bm, t):
            if bm == tot:
                return 0
            ret = -10**9 if t else 10**9
            f = max if t else min
            for i in range(len(positions)):
                if not bm & 1 << i:
                    ret = f(ret, dist[cx, cy][positions[i][0], positions[i][1]] + dp(positions[i][0], positions[i][1], bm ^ 1 << i, 1-t))
            return ret

        return dp(kx, ky, 0, 1)
                    