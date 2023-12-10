

dist = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for x, y, z in roads:
    dist[x][y] = min(dist[x][y], z)
    dist[y][x] = min(dist[y][x], z)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]