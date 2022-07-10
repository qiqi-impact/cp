class Solution:
    def countPaths(self, m: List[List[int]]) -> int:
        R, C = len(m), len(m[0])
        
        q = []
        for i in range(R):
            for j in range(C):
                q.append((m[i][j], i, j))
        q.sort()
        
        D = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        d = defaultdict(int)
        for v, x, y in q:
            d[x, y] += 1
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and m[nx][ny] > v:
                    d[nx, ny] += d[x, y]
        return sum(d.values()) % (10**9+7)