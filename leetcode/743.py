class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in times:
            x -= 1
            y -= 1
            g[x].append((y, w))
        dist = [inf for _ in range(n)]
        dist[k-1] = 0
        h = [(0, k-1)]
        while h:
            cost, cur = heapq.heappop(h)
            if dist[cur] != cost:
                continue
            for y, w in g[cur]:
                if cost + w < dist[y]:
                    dist[y] = cost + w
                    heapq.heappush(h, (cost + w, y))
        mx = 0
        for i in range(n):
            if dist[i] == inf:
                return -1
            mx = max(mx, dist[i])
        return mx