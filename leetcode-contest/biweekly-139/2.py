class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        R, C = len(grid), len(grid[0])
        if grid[0][0]:
            health -= 1

        START = 0, (0, 0)
        END = (R-1, C-1)
        h = [START]
        dist = {START[1]: 0}
        while h:
            cost, cur = heapq.heappop(h)
            x, y = cur
            if dist[cur] != cost:
                continue
            if cur == END:
                return cost < health
            for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C:
                    o = (nx, ny)
                    w = grid[nx][ny]
                    if dist.get(o, inf) > cost + w:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))