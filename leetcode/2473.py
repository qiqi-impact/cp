class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        g = [{} for _ in range(n)]
        for x, y, w in roads:
            x -= 1
            y -= 1
            g[x][y] = g[y][x] = w
        
        def dijk(root):
            mincost = inf
            dist = [inf for _ in range(n)]
            dist[root] = 0
            h = [(0, root)]
            while h:
                c, v = heapq.heappop(h)
                if c != dist[v]:
                    continue
                if (k+1) * c > mincost:
                    break
                mincost = min(mincost, appleCost[v] + (k+1) * c)
                for o in g[v]:
                    if dist[o] > dist[v] + g[v][o]:
                        dist[o] = dist[v] + g[v][o]
                        heapq.heappush(h, (dist[o], o))
            return mincost
        
        ret = [dijk(i) for i in range(n)]
        return ret