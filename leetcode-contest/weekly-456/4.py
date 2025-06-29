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
        return a != b

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        l = []
        edges.sort(key=lambda x:-x[2])
        dsu = DisjointSetUnion(n)
        mn = inf
        for a, b, c, d in edges:
            if d == 1:
                if not dsu.union(a, b):
                    return -1
                mn = min(mn, c)
        for a, b, c, d in edges:
            if d == 0:
                if not dsu.union(a, b):
                    continue
                l.append(c)
        l.sort()
        if dsu.set_size(0) != n:
            return -1
        if not l:
            return mn
        if k == 0:
            return min(mn, l[0])
        if k >= len(l):
            return min(mn, 2 * l[0])
        return min(mn, l[k], 2 * l[0])