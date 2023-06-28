class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = [[] for _ in range(n)]
        for i, (x, y) in enumerate(edges):
            z = succProb[i]
            if z > 0:
                g[x].append((y, z))
                g[y].append((x, z))
        h = [(1, start)]
        dist = {start: 1}
        while h:
            d, cur = heapq.heappop(h)
            if dist[cur] != d:
                continue
            if cur == end:
                return 1/d
            for nei, z in g[cur]:
                nd = d * 1/z
                if dist.get(nei, inf) > nd:
                    dist[nei] = nd
                    heapq.heappush(h, (nd, nei))
        return 0