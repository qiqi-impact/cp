class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n, m = len(edges1)+1, len(edges2)+1

        gg = [[] for _ in range(m)]
        for x, y in edges2:
            gg[x].append(y)
            gg[y].append(x)
        
        g = [[] for _ in range(n)]
        for x, y in edges1:
            g[x].append(y)
            g[y].append(x)

        
        def bfs(node, gr, par):
            color = [None] * len(gr)
            dist = [inf] * len(gr)
            dist[node] = 0
            ct = int(par == 0)
            color[0] = 0
            q = deque([node])
            while q:
                cur = q.popleft()
                for ch in gr[cur]:
                    if dist[ch] == inf:
                        color[ch] = 1 - color[cur]
                        ct += (dist[cur]+1) % 2 == par
                        dist[ch] = dist[cur] + 1
                        q.append(ch)
            return ct, color

        l, _ = bfs(0, gg, 1)
        t = max(l, m-l)

        a, col = bfs(0, g, 0)
        ret = []
        for i in range(n):
            if col[i] == 0:
                ret.append(a + t)
            else:
                ret.append(n - a + t)
        return ret