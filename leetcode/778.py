class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if R*C == 1:
            return grid[0][0]
        uf = UnionFind(R*C)
        l = []
        for i in range(R):
            for j in range(C):
                l.append((grid[i][j], i, j))
        l.sort()
        for i in range(len(l)):
            t, x, y = l[i]
            for dx, dy in itertools.pairwise([-1, 0, 1, 0, -1]):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] <= t:
                    uf.union(x*C+y, nx*C+ny)
            if uf.find(0) == uf.find(R*C-1):
                return t