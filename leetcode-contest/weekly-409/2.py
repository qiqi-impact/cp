class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n-1):
            g[i].append(i+1)
        
        def bfs():
            q = deque([0])
            dist = {0: 0}
            while q:
                v = q.popleft()
                for x in g[v]:
                    if x not in dist:
                        dist[x] = dist[v] + 1
                        q.append(x)
            return dist[n-1]
        
        ret = []
        for x, y in queries:
            g[x].append(y)
            ret.append(bfs())
        return ret