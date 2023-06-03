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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [[i]+e[:] for i,e in enumerate(edges)]

        edges.sort(key=lambda x:x[3])
        crit, ps = [], []

        base = 0
        dsu = DisjointSetUnion(n)
        for _,(i,x,y,w) in enumerate(edges):
            if dsu.find(x) != dsu.find(y):
                base += w
                dsu.union(x, y)

        for idx in range(len(edges)):
            cost_without = 0
            dsu = DisjointSetUnion(n)
            amt = 0
            for q,(i,x,y,w) in enumerate(edges):
                if q == idx:
                    continue
                if dsu.find(x) != dsu.find(y):
                    cost_without += w
                    amt += 1
                    dsu.union(x, y)
            if amt != n-1:
                crit.append(edges[idx][0])
                continue
            
            cost_with = edges[idx][3]
            dsu = DisjointSetUnion(n)
            dsu.union(edges[idx][1], edges[idx][2])
            for q,(i,x,y,w) in enumerate(edges):
                if q == idx:
                    continue
                if dsu.find(x) != dsu.find(y):
                    cost_with += w
                    dsu.union(x, y)

            if cost_with > base:
                continue
            
            if cost_with == cost_without:
                ps.append(edges[idx][0])
            else:
                crit.append(edges[idx][0])

        return [crit, ps]