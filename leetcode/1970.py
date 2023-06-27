class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def latestDayToCross(self, R: int, C: int, cells: List[List[int]]) -> int:
        dsu = DisjointSetUnion(R*C+2)
        left, right = R*C, R*C+1
        seen = set()
        for i, (x, y) in enumerate(cells):
            x -= 1
            y -= 1
            seen.add((x, y))
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < R and 0 <= ny < C and (nx, ny) in seen:
                            dsu.union(x*C+y, nx*C+ny)
            if y == 0:
                dsu.union(x*C+y, left)
            if y == C-1:
                dsu.union(x*C+y, right)
            if dsu.find(left) == dsu.find(right):
                return i