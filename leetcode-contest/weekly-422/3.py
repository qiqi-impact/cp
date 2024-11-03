class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R, C = len(moveTime), len(moveTime[0])
        dist = {(0,0,0):0}
        h = [(0,0,0,0)]
        while h:
            c,x,y,p = heapq.heappop(h)
            if (x,y) == (R-1, C-1):
                return c
            if dist[(x,y,p)] != c:
                continue
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and dist.get((nx,ny,1-p), inf) > p + 1 + max(moveTime[nx][ny], c):
                    dist[nx,ny,1-p] = p + 1 + max(moveTime[nx][ny], c)
                    heapq.heappush(h, (dist[nx,ny,1-p], nx, ny, 1-p))
                