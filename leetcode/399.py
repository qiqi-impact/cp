class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        
        for i, (x, y) in enumerate(equations):
            v = values[i]
            if x not in g:
                g[x] = []
            if y not in g:
                g[y] = []
            if x == y:
                continue
            g[x].append((y, 1/v))
            g[y].append((x, v))
        
        def dfs(x, v, c):
            values[x] = (c, v)
            for y, z in g[x]:
                if y not in values:
                    dfs(y, z * v, c)
        
        values = {}
        ct = 0
        for k in g:
            if k not in values:
                dfs(k, 1, ct)
                ct += 1
            
        ret = []
        for x, y in queries:
            if x not in g or y not in g or (values[x][0] != values[y][0]):
                ret.append(-1)
            else:
                ret.append(values[x][1] / values[y][1])
        return ret
                