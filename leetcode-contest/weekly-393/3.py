class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        
        g = [{} for _ in range(n)]
        for x, y, w in edges:
            g[x][y] = g[y][x] = min(g[x].get(y, inf), w)
            
        fail = set()
            
        START = 0, 0
        h = [START]
        dist = {START[1]: 0}
        while h:
            cost, cur = heapq.heappop(h)
            if dist[cur] != cost:
                continue
            if cost >= disappear[cur]:
                fail.add(cur)
                continue
            for o in g[cur]:
                w = g[cur][o]
                if dist.get(o, inf) > cost + w:
                    dist[o] = cost + w
                    heapq.heappush(h, (cost + w, o))
                    
        for x in fail:
            dist[x] = -1
            
        ret = [-1] * n
        for x in dist:
            ret[x] = dist[x]
        return ret