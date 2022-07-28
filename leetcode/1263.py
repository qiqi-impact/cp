class Solution:
    def minPushBox(self, g: List[List[str]]) -> int:
        R, C = len(g), len(g[0])
        
        for i in range(R):
            for j in range(C):
                if g[i][j] == 'S':
                    pi, pj = i, j
                elif g[i][j] == 'B':
                    bi, bj = i, j
                elif g[i][j] == 'T':
                    ti, tj = i, j
        
        v = (pi, pj, bi, bj)
        seen = set([v])
        h = [(0, *v)]

        while h:
            m, ax, ay, bx, by = heapq.heappop(h)
            for dx, dy in pairwise([-1, 0, 1, 0, -1]):
                nx, ny = ax+dx, ay+dy
                if 0 <= nx < R and 0 <= ny < C and g[nx][ny] != '#':
                    nbx, nby = bx, by
                    nm = m
                    if (nx, ny) == (bx, by):
                        nbx += dx
                        nby += dy
                        nm += 1
                        if not (0 <= nbx < R and 0 <= nby < C and g[nbx][nby] != '#'):
                            continue
                    if (nbx, nby) == (ti, tj):
                        return nm
                    v = (nx, ny, nbx, nby)
                    if v not in seen:
                        seen.add(v)
                        heapq.heappush(h, (nm, *v))
        return -1