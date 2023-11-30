class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        e = {}
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(R):
            for j in range(C):
                e[i,j] = {}
                for q in range(4):
                    dx, dy = direction[q]
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < R and 0 <= ny < C:
                        e[i,j][nx,ny] = int(q+1 != grid[i][j])
        
        START = 0, (0,0)
        END = (R-1, C-1)
        h = [START]
        dist = {START[1]: 0}
        while h:
            cost, cur = heapq.heappop(h)
            if dist[cur] != cost:
                continue
            if cur == END:
                return cost
            for o, w in e[cur].items():
                if dist.get(o, inf) > cost + w:
                    dist[o] = cost + w
                    heapq.heappush(h, (cost + w, o))
        return -1