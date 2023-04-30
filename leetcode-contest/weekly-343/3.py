class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        start = tuple(start)
        target = tuple(target)
        edges = {start:{}, target:{}}
        
        for a, b, c, d, w in specialRoads:
            p = a, b
            q = c, d
            if p not in edges:
                edges[p] = {}
            if q not in edges:
                edges[q] = {}
            if abs(p[1]-q[1]) + abs(p[0]-q[0]) <= w:
                continue
            edges[p][q] = min(edges[p].get(q, inf), w)

            
        l = list(edges.keys())
        for i in range(len(l)):
            p = l[i]
            for j in range(i+1, len(l)):
                q = l[j]
                if q not in edges[p]:
                    edges[p][q] = abs(p[1]-q[1]) + abs(p[0]-q[0])
                if p not in edges[q]:
                    edges[q][p] = abs(p[1]-q[1]) + abs(p[0]-q[0])

        
        START = 0, start
        END = target
        h = [START]
        dist = {START[1]: 0}
        while h:
            cost, cur = heapq.heappop(h)
            if dist[cur] != cost:
                continue
            if cur == END:
                return cost
            for o in edges[cur]:
                w = edges[cur][o]
                if dist.get(o, inf) > cost + w:
                    dist[o] = cost + w
                    heapq.heappush(h, (cost + w, o))