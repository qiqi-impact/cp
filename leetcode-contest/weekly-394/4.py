class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [{} for _ in range(n)]
        for x, y, w in edges:
            g[x][y] = g[y][x] = min(g[x].get(y, inf), w)

            
        def dijk(x):
            START = 0, x
            # END = y
            h = [START]
            dist = {START[1]: 0}
            while h:
                cost, cur = heapq.heappop(h)
                if dist[cur] != cost:
                    continue
                # if cur == END:
                #     return cost
                for o, w in g[cur].items():
                    if dist.get(o, inf) > cost + w:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))
            return dist
        
        A = dijk(0)
        B = dijk(n-1)
        m = len(edges)
        ret = [False] * m
        if n-1 not in A:
            return ret
        t = A[n-1]
        for i, (x, y, w) in enumerate(edges):
            if x in A and y in B:
                if A[x] + B[y] + w == t:
                    ret[i] = True
            if x in B and y in A:
                if B[x] + A[y] + w == t:
                    ret[i] = True
        return ret
        