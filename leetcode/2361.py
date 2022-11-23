class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        h = [(0, 0, 0)]
        dist = {(0, 0): 0}
        
        ret = [inf] * len(regular)
        
        while h:
            c, a, b = heapq.heappop(h)
            if dist[a, b] != c:
                continue
            if a > 0:
                ret[a-1] = min(ret[a-1], c)
            opt = []
            if b == 1:
                opt.append([c, a, 1-b])
            else:
                opt.append([c+expressCost, a, 1-b])
            if a != len(regular):
                if b == 1:
                    opt.append([c + express[a], a+1, b])
                else:
                    opt.append([c + regular[a], a+1, b])
            for nc, na, nb in opt:
                if nc < dist.get((na, nb), inf):
                    dist[na, nb] = nc
                    heapq.heappush(h, (nc, na, nb))
        return ret