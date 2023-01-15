class DisjointSetUnion:
    def __init__(self, n, arr):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
        self.mxv = arr[:]
        self.ct = [1] * n

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
            
            if self.mxv[a] == self.mxv[b]:
                self.ct[a] += self.ct[b]
            elif self.mxv[a] < self.mxv[b]:
                self.mxv[a] = self.mxv[b]
                self.ct[a] = self.ct[b]
        return a

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        dsu = DisjointSetUnion(n, vals)
        vd = defaultdict(list)
        for i, v in enumerate(vals):
            vd[v].append(i)
        ret = 0
        for v in sorted(vd.keys()):
            rr = set()
            for x in vd[v]:
                for o in g[x]:
                    if vals[o] <= v:
                        rr.add(dsu.union(x, o))
            roots = {dsu.find(x) for x in rr}
            for r in roots:
                if dsu.mxv[r] == v:
                    x = dsu.ct[r]
                    ret += x * (x - 1) // 2
        return ret + n