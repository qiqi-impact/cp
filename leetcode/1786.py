class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            x -= 1
            y -= 1
            g[x].append((y, w))
            g[y].append((x, w))

        START = 0, n-1
        h = [START]
        dist = {START[1]: 0}
        while h:
            cost, cur = heapq.heappop(h)
            if dist[cur] != cost:
                continue
            for o, w in g[cur]:
                if dist.get(o, inf) > cost + w:
                    dist[o] = cost + w
                    heapq.heappush(h, (cost + w, o))
        
        @cache
        def dp(idx):
            ret = 1 if idx == 0 else 0
            for x, _ in g[idx]:
                if dist[x] > dist[idx]:
                    ret += dp(x)
                    ret %= 10**9+7
            return ret

        return dp(n-1)