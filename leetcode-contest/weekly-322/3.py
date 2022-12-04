class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ret = inf
        
        g = [[] for _ in range(n)]
        for x, y, z in roads:
            x -= 1
            y -= 1
            g[x].append((y, z))
            g[y].append((x, z))

        vis = set()
        def dfs(idx):
            nonlocal ret
            vis.add(idx)
            for o, w in g[idx]:
                ret = min(ret, w)
                if o not in vis:
                    dfs(o)
        dfs(0)
        
        return ret