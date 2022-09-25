class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
        self.freq = [defaultdict(int) for _ in range(n)]

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b, v):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
            
            q = self.freq[a][v] * self.freq[b][v]
            
            for k in self.freq[b]:
                self.freq[a][k] += self.freq[b][k]
            return q
        return 0

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        dsu = DisjointSetUnion(n)
        
        for i in range(n):
            dsu.freq[i][vals[i]] = 1
        
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        s = defaultdict(list)
        for i, v in enumerate(vals):
            s[v].append(i)
            
        seen = set()
        ret = 0
        for k in sorted(list(s.keys())):
            for x in s[k]:
                seen.add(x)
                for y in g[x]:
                    if y in seen:
                        ret += dsu.union(x, y, k)
                        # print(x, y, ret)
        return ret + n
                        
        
        
        