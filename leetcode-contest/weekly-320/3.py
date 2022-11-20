from collections import deque

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        g = [[] for _ in range(n)]
        prev = [-1 for _ in range(n)]
        deg = [0 for _ in range(n)]
        # dist = [inf for _ in range(n)]
        amt = [1 for _ in range(n)]

        q = deque()
        
        for x, y in roads:
            # x -= 1
            # y -= 1
            g[x].append(y)
            g[y].append(x)
            
        def dfs(node, p, dst):
            # dist[node] = dst
            for o in g[node]:
                if o != p:
                    prev[o] = node
                    deg[node] += 1
                    dfs(o, node, dst+1)
            if deg[node] == 0:
                q.append(node)
        dfs(0, -1, 0)
        
        ret = 0
        while q:
            cur = q.popleft()
            if cur == 0:
                return ret
            ret += (amt[cur] + seats - 1)//seats
            amt[prev[cur]] += amt[cur]
            deg[prev[cur]] -= 1
            if deg[prev[cur]] == 0:
                q.append(prev[cur])
        return ret
        
        