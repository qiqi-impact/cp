import itertools

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        R, C = len(grid), len(grid[0])
        
        tot = 0
        for i in range(R):
            for j in range(C):
                if 'a' <= grid[i][j] <= 'f':
                    tot |= (1 << (ord(grid[i][j])-97))
                if grid[i][j] == '@':
                    sx, sy = i, j
        
        dist = {(0, sx, sy): 0}
        q = deque()
        q.append((0, sx, sy))
        while q:
            ok, x, y = q.popleft()
            for dx, dy in itertools.pairwise([-1, 0, 1, 0, -1]):
                nx, ny = x+dx, y+dy
                keys = ok
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != '#':
                    v = grid[nx][ny]
                    if 'a' <= v <= 'f':
                        keys |= (1 << (ord(v)-97))
                    elif 'A' <= v <= 'F':
                        if not keys & (1 << (ord(v)-ord('A'))):
                            continue
                    if (keys, nx, ny) not in dist:
                        dist[keys, nx, ny] = 1 + dist[ok, x, y]
                        if keys == tot:
                            return dist[keys, nx, ny]
                        q.append((keys, nx, ny))
        return -1