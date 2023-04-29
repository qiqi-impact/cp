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
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        l = []
        for i, x in enumerate(bloomDay):
            l.append((x, i))
        l.sort()
        dsu = DisjointSetUnion(n)

        cur = 0

        vis = set()

        for x, i in l:
            cur += dsu.set_size(i)//k
            if i > 0 and i-1 in vis:
                cur -= dsu.set_size(i)//k
                cur -= dsu.set_size(i-1)//k
                dsu.union(i, i-1)
                cur += dsu.set_size(i)//k
            if i < n-1 and i+1 in vis:
                cur -= dsu.set_size(i)//k
                cur -= dsu.set_size(i+1)//k
                dsu.union(i, i+1)
                cur += dsu.set_size(i)//k
            vis.add(i)
            if cur >= m:
                return x

        