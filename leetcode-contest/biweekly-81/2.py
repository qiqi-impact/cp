class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        vis = set()
        
        g = defaultdict(set)
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
        
        def dfs(i, p):
            ret = 1
            for other in g[i]:
                if other != p and other not in vis:
                    vis.add(other)
                    ret += dfs(other, i)
            return ret
        
        ret = 0
        for i in range(n):
            if i not in vis:
                vis.add(i)
                s = dfs(i, -1)
                ret += s * (n - s)
        ret //= 2
        return ret
            
            