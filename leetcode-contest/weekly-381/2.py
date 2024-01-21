class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        
        x -= 1
        y -= 1
        
        
        roads = [(x, y, 1)]
        for i in range(n-1):
            roads.append((i, i+1, 1))
        
        
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
                        
        ret = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j:
                    ret[dist[i][j]-1] += 1
        return ret