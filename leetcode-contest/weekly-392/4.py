class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
        self.x = [2**64-1] * n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b, w):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
        self.x[a] &= self.x[b] & w

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DisjointSetUnion(n)
        
        for x, y, w in edges:
            dsu.union(x, y, w)
                
        ret = []
        for x, y in query:
            fx, fy = dsu.find(x), dsu.find(y)
            if x == y:
                ret.append(0)
            elif fx != fy:
                ret.append(-1)
            else:
                ret.append(dsu.x[fx])
        return ret