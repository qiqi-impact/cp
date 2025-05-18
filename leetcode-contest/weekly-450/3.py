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
            if ord('A') <= ord(m[x][y]) <= ord('Z'):
                for (i, j) in tele[m[x][y]]:
                    if (i, j) != (x, y) and (i, j) not in dist:
                        dist[(i, j)] = c
                        q.append((c, i, j))
                    if (i, j) == (0, 0):
                        return dist[(i, j)]
        r = tele_expand(0, R-1, C-1)
        if r is not None:
            return r

        while q:
            c, x, y = q.popleft()
            for dx, dy in pairwise([1,0,-1,0,1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and m[nx][ny] != '#' and (nx, ny) not in dist:
                    dist[(nx, ny)] = c + 1
                    if (nx, ny) == (0, 0):
                        return dist[(nx, ny)]
                    q.append((c+1, nx, ny))
                    r = tele_expand(c+1, nx, ny)
                    if r is not None:
                        return r
        return -1