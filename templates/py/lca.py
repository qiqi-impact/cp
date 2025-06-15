MX = 17 # 10**5

g = [[] for _ in range(n)]
for x, y, w in edges:
    g[x].append((y, w))
    g[y].append((x, w))

depth = [0] * n
weight_depth = [0] * n
p = [[0 for _ in range(n)]]

def dfs(x, q, dp, wdp):
    p[0][x] = q
    depth[x] = dp
    weight_depth[x] = wdp
    for ch, w in g[x]:
        if ch != q:
            dfs(ch, x, dp+1, wdp + w)
dfs(0, 0, 0, 0)

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

def get_anc(x, amt):
    cur = x
    for i in range(MX-1, -1, -1):
        if amt & 1 << i:
            cur = p[i][cur]
    return cur

def cost(x, y):
    return weight_depth[x] + weight_depth[y] - 2 * weight_depth[lca(x, y)]
