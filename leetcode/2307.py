class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        g = {}
        n = len(equations)
        for i in range(n):
            x, y = equations[i]
            w = values[i]
            if x not in g: g[x] = {}
            if y not in g: g[y] = {}
            if x in g[y] and g[y][x] != 1/w:
                return True
            if y in g[x] and g[x][y] != w:
                return True
            g[x][y] = w
            g[y][x] = 1/w

        def dfs(x):
            for y in g[x]:
                if y in val:
                    if abs(val[y] - val[x] * g[y][x]) >= 10**-5:
                        return True
                else:
                    val[y] = val[x] * g[y][x]
                    if dfs(y):
                        return True
            return False

        val = {}
        for k in g:
            if k not in val:
                val[k] = 1.
                if dfs(k):
                    return True
        return False