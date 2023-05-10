class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[None for _ in range(n)] for _ in range(n)]
        vis = [[0 for _ in range(n)] for _ in range(n)]
        cx, cy = 0, -1
        cur = 0
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        dp = 0
        for i in range(1, 1+n*n):
            dx, dy = d[dp]
            nx, ny = cx+dx, cy+dy
            if not (0 <= nx < n and 0 <= ny < n and not vis[nx][ny]):
                dp += 1
                dp %= 4
                dx, dy = d[dp]
                nx, ny = cx+dx, cy+dy
            vis[nx][ny] = 1
            cx, cy = nx, ny
            ret[cx][cy] = i
        return ret
