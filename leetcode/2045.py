from collections import deque

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            x -= 1
            y -= 1
            g[x].append(y)
            g[y].append(x)
            
        dist = [inf for _ in range(n)]
        vis = [False for _ in range(n)]
        dist[0] = 0
        
        cost = 2
        
        q = deque([(0, 0)])
        while q:
            i, c = q.popleft()
            for x in g[i]:
                if c + 1 < dist[x]:
                    dist[x] = c + 1
                    q.append((x, c+1))
                elif c + 1 == dist[x] + 1 and not vis[x]:
                    if x == n-1:
                        cost = 1
                        break
                    vis[x] = True
                    q.append((x, c+1))
            if cost == 1:
                break
        
        cost += dist[n-1]
        
        t = 0
        for i in range(cost):
            if (t // change) % 2:
                t = ((t // change) + 1) * change
            t += time
        return t