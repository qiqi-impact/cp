class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        colors = [ord(c)-97 for c in colors]
        
        n = len(colors)
        g = [[] for _ in range(n)]
        ind = [0 for _ in range(n)]
        ct = [[0] * 26 for _ in range(n)]
        
        for x, y in edges:
            g[x].append(y)
            ind[y] += 1
        
        vis = [False] * n
        q = deque()
        for i in range(n):
            if ind[i] == 0:
                q.append(i)
                vis[i] = True
                ct[i][colors[i]] = 1
        
        mx = 1
        while q:
            cur = q.popleft()
            for o in g[cur]:
                ind[o] -= 1
                for i in range(26):
                    ct[o][i] = max(ct[o][i], ct[cur][i])
                if ind[o] == 0:
                    vis[o] = True
                    ct[o][colors[o]] += 1
                    mx = max(mx, ct[o][colors[o]])
                    q.append(o)
        for x in vis:
            if not x:
                return -1
        return mx
        