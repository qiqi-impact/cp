MX = 32

g = [[] for _ in range(n)]
for x, y in edges:
    w -= 1
    g[x].append(y)
    g[y].append(x)

depth = [0] * n

def dfs(x, q, dp):
    p[0][x] = q
    depth[x] = dp
    for ch, w in g[x]:
        if ch != q:
            dfs(ch, x, dp+1)
dfs(0, 0, 0)

p = [[0 for _ in range(n)]]
for _ in range(MX):
    pp = [p[-1][p[-1][i]] for i in range(n)]
    p.append(pp)

def lca(x, y):
    if depth[x] < depth[y]:
        x, y = y, x
    for i in range(MX):
        if (depth[x]-depth[y]) & (1 << i):
            x = p[i][x]
    if x == y:
        return x
    for i in range(MX-1, -1, -1):
        if p[i][x] != p[i][y]:
            x, y = p[i][x], p[i][y]
    return p[0][x]