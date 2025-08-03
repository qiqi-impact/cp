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
    def minTime(self, s: str, order: List[int], k: int) -> int:
        n = len(order)
        dsu = DisjointSetUnion(n)
        ret = (n+1) * n // 2
        if ret < k:
            return -1
        vis = [0] * n
        for i in range(n-1, -1, -1):
            o = order[i]
            vis[o] = 1
            ret -= 1
            for x in o-1, o+1:
                if 0 <= x < n and vis[x]:
                    t = dsu.set_size(x)
                    u = dsu.set_size(o)
                    ret -= t * u
                    dsu.union(o, x)
            if ret < k:
                return i


        