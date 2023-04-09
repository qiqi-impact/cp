class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        cols = [[] for _ in range(C)]

        for i in range(R):
            h = []
            for j in range(C):
                if i+j == 0:
                    cost = 1
                    h.append((1, grid[i][j]))
                    cols[0].append((1, grid[i][j]))
                    continue
                while h and h[0][1] < j:
                    heapq.heappop(h)
                while cols[j] and cols[j][0][1] < i:
                    heapq.heappop(cols[j])
                cost = inf
                if h:
                    cost = min(cost, h[0][0] + 1)
                if cols[j]:
                    cost = min(cost, cols[j][0][0] + 1)
                if cost < inf:
                    heapq.heappush(h, (cost, j + grid[i][j]))
                    heapq.heappush(cols[j], (cost, i + grid[i][j]))
            
        return -1 if cost == inf else cost