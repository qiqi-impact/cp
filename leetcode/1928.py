class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        
        g = defaultdict(dict)
        for x, y, w in edges:
            g[x][y] = min(g[x].get(y, float('inf')), w)
            g[y][x] = min(g[y].get(x, float('inf')), w)
        
        memo = {(0, 0): passingFees[0]}
        h = [(passingFees[0], 0, 0)]
        while h:
            cost, idx, t = heappop(h)
            idx = -idx
            if idx == n-1:
                return cost
            if memo[idx, t] != cost:
                continue
            for other in g[idx]:
                nt = t + g[idx][other]
                new_cost = cost + passingFees[other]
                if nt <= maxTime and new_cost < memo.get((other, nt), float('inf')):
                    memo[(other, nt)] = new_cost
                    heappush(h, (new_cost, -other, nt))
        return -1