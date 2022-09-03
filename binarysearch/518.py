class Solution:
    def solve(self, edges):
        g = {}
        n = 0
        for u, v, w in edges:
            if u not in g:
                g[u] = {}
            if v not in g:
                g[v] = {}
            g[u][v] = min(g[u].get(v, float('inf')), w)
            g[v][u] = min(g[v].get(u, float('inf')), w)
            n = max(n, u, v)
        n += 1

        mc = defaultdict(int)
        h = [(0, 0, 0, 0)]
        mc[0, 0] = 0
        while h:
            cost, idx, me, ne = heappop(h)
            if idx == n-1:
                return cost
            if mc[idx, me] != cost:
                continue
            for other in g.get(idx, {}):
                w = g[idx][other]
                new_mx = max(me, w)
                new_ne = ne + 1
                new_cost = new_mx * new_ne
                if new_cost < mc.get((other, new_mx), float('inf')):
                    mc[other, new_mx] = new_cost
                    heappush(h, (new_cost, other, new_mx, new_ne))
        return -1