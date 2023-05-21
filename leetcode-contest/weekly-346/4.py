class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], A: int, B: int, target: int) -> List[List[int]]:
        g = [{} for _ in range(n)]
        
        fr = []
        
        for x, y, w in edges:
            if w == -1:
                fr.append([x, y])
            else:
                g[x][y] = g[y][x] = w
                
        def dijk():
            START = 0, A
            END = B
            h = [START]
            dist = {START[1]: 0}
            while h:
                cost, cur = heapq.heappop(h)
                if dist[cur] != cost:
                    continue
                if cur == END:
                    return cost
                for o, w in g[cur].items():
                    if dist.get(o, inf) > cost + w:
                        dist[o] = cost + w
                        heapq.heappush(h, (cost + w, o))
            return inf
        
        cur = dijk()
        found = False
        if cur < target:
            return []
        elif cur == target:
            found = True
        
        for p, (x, y) in enumerate(fr):
            if found:
                g[x][y] = g[y][x] = 2 * (10**9)
                continue

            g[x][y] = g[y][x] = 1
            nx = dijk()
            if nx > target:
                continue

            a, b = 1, 2*(10**9)
            while a < b:
                mi = (a+b)//2
                g[x][y] = g[y][x] = mi
                q = dijk()
                if q == target:
                    found = True
                    break
                elif q < target:
                    a = mi
                else:
                    b = mi

            if not found:
                g[x][y] = g[y][x] = 1
                
        if not found:
            return []
            
        ret = []
        for i in range(n):
            for x in g[i]:
                if x > i:
                    ret.append([i,x,g[i][x]])
        return ret
            