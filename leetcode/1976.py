class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = [{} for _ in range(n)]
        for x, y, t in roads:
            g[x][y] = g[y][x] = t

        START = 0, 0
        END = n-1
        h = [START]
        dist = {START[1]: 0}
        while h:
            cost, cur = heapq.heappop(h)
            if dist[cur] != cost:
                continue
            if cur == END:
                break
            for o in g[cur]:
                w = g[cur][o]
                if dist.get(o, inf) > cost + w:
                    dist[o] = cost + w
                    heapq.heappush(h, (cost + w, o))

        @cache
        def dp(idx):
            if idx == n-1:
                return 1
            ret = 0
            for o in g[idx]:
                t = g[idx][o]
                if t + dist[idx] == dist.get(o, inf):
                    ret += dp(o)
            ret %= 10**9+7
            return ret

        return dp(0)


