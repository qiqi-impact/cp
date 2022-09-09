class Solution:
    def solve(self, sets, removals):
        g = {}
        n = len(removals)
        for x, y, w in sets:
            if x not in g:
                g[x] = {}
            g[x][y+1] = min(g[x].get(y+1, float('inf')), w)
        for i in range(n-1, -1, -1):
            if i+1 not in g:
                g[i+1] = {}
            g[i+1][i] = removals[i]
        
        h = [(0, 0)]
        cost = [float('inf')] * (n+1)
        cost[0] = 0
        while h:
            c, x = heappop(h)
            if x == n:
                return c
            if c != cost[x]:
                continue
            if x in g:
                for y in g[x]:
                    w = g[x][y]
                    if c + w < cost[y]:
                        heappush(h, (c+w, y))
                        cost[y] = c+w
        return -1