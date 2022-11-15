class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        
        g = {}
        for x, y, c in flights:
            if x not in g:
                g[x] = {}
            if y not in g[x]:
                g[x][y] = c
        
        dist = {(src, 0) : 0}
        h = [(0, src, 0)]
        while h:
            c, x, s = heapq.heappop(h)
            print(c, x, s)
            if c != dist[(x, s)]:
                continue
            if x == dst:
                return c
            if s <= k:
                for o in g.get(x, {}):
                    nc = c + g[x][o]
                    ns = s + 1
                    if (o, ns) not in dist or dist[o, ns] > nc:
                        dist[o, ns] = nc
                        heapq.heappush(h, (nc, o, ns))
        return -1