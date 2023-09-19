class Solution:
    def shortestPathLength(self, g: List[List[int]]) -> int:
        q = deque()
        n = len(g)
        FULL = (1 << n) - 1
        dist = {}
        for i in range(n):
            q.append((i, 1 << i))
            dist[(i, 1 << i)] = 0
        while q:
            cur, seen = q.popleft()
            for x in g[cur]:
                nx = x, seen | (1 << x)
                if nx not in dist:
                    dist[nx] = 1 + dist[cur, seen]
                    if nx[1] == FULL:
                        return dist[nx]
                    q.append(nx)
        return 0