class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        mx = 0
        N = len(values)
        
        g = [{} for _ in range(N)]
        
        for x, y, z in edges:
            g[x][y] = g[y][x] = z
        
        tm = 0
        seen = defaultdict(int)
        seen[0] = 1
        score = values[0]
        def dfs(idx):
            nonlocal tm, mx, score
            if idx == 0:
                mx = max(mx, score)
            for other in g[idx]:
                c = g[idx][other]
                if c + tm <= maxTime:
                    tm += c
                    seen[other] += 1
                    if seen[other] == 1:
                        score += values[other]
                    dfs(other)
                    seen[other] -= 1
                    if seen[other] == 0:
                        score -= values[other]
                    tm -= c
        dfs(0)
        return mx