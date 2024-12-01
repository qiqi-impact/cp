class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1

        gg = [[] for _ in range(m)]
        for x, y in edges2:
            gg[x].append(y)
            gg[y].append(x)
        
        g = [[] for _ in range(n)]
        for x, y in edges1:
            g[x].append(y)
            g[y].append(x)

        def bfs(node, gr, kk):
            if kk == -1:
                return 0
            dist = [inf] * len(gr)
            dist[node] = 0
            ct = 1
            q = deque([node])
            while q:
                cur = q.popleft()
                if dist[cur] == kk:
                    break
                for ch in gr[cur]:
                    if dist[ch] == inf:
                        ct += 1
                        dist[ch] = dist[cur] + 1
                        q.append(ch)
            return ct

        l = [bfs(idx, gg, k-1) for idx in range(m)]
        m = max(l)

        return [bfs(idx, g, k) + m for idx in range(n)]
                
                        
            




        
        