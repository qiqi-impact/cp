n = len(edges)
adj = [[] for _ in range(n)]
adj_rev = [[] for _ in range(n)]
for x, y in edges:
    adj[x].append(y)
    adj_rev[y].append(x)
order = []
component = []
used = [False] * n

def dfs1(v):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs1(u)
    order.append(v)

def dfs2(v):
    used[v] = True
    component.append(v)
    for u in adj_rev[v]:
        if not used[u]:
            dfs2(u)

for i in range(n):
    if not used[i]:
        dfs1(i)

order = order[::-1]
used = [False] * n
components = []

for v in order:
    if not used[v]:
        dfs2(v)
        components.append(component)
        component = []