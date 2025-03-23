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
            return True
        return False

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def numberOfComponents(self, A: List[List[int]], k: int) -> int:
        n = len(A)
        dsu = DisjointSetUnion(n)
        l = [set(p) for p in A]
        ret = n
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                x = l[i] & l[j]
                if len(x) >= k:
                    if dsu.union(i, j):
                        ret -= 1
        return ret
                    



        