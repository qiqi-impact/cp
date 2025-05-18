class Solution:
    def minMoves(self, m: List[str]) -> int:

        tele = defaultdict(list)
        
        R, C = len(m), len(m[0])
        if R == 1 and C == 1:
            return 0
        if m[R-1][C-1] == '#':
            return -1

        for i in range(R):
            for j in range(C):
                if ord('A') <= ord(m[i][j]) <= ord('Z'):
                    tele[m[i][j]].append((i, j))
        
        dist = {
            (R-1, C-1): 0
        }
        q = deque([(0, R-1, C-1)])

        def tele_expand(c, x, y):
            if m[x][y] in tele:
                for (i, j) in tele[m[x][y]]:
                    if (i, j) != (x, y) and dist.get((i, j), inf) > c:
                        dist[(i, j)] = c
                        q.appendleft((c, i, j))
                del tele[m[x][y]]

        while q:
            c, x, y = q.popleft()
            if (x, y) == (0, 0):
                return c
            if c != dist[(x, y)]:
                continue
            r = tele_expand(c, x, y)
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and m[nx][ny] != '#' and dist.get((nx, ny), inf) > c + 1:
                    dist[(nx, ny)] = c + 1
                    q.append((c+1, nx, ny))
                    if r is not None:
                        return r
        return -1