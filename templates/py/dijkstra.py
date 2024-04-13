g = [{} for _ in range(n)]
for x, y, w in edges:
    g[x][y] = g[y][x] = min(g[x].get(y, inf), w)

START = 0, x
END = y
h = [START]
dist = {START[1]: 0}
while h:
    cost, cur = heapq.heappop(h)
    if dist[cur] != cost:
        continue
    if cur == END:
        return cost
    for o, w in g[cur].items():
        if dist.get(o, inf) > cost + w:
            dist[o] = cost + w
            heapq.heappush(h, (cost + w, o))
return -1