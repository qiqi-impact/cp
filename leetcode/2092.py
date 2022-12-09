class UnionFind:
    def __init__(self, L):
        self.parent = {x:x for x in L}

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
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        know = set([0, firstPerson])
        
        d = defaultdict(list)
        v = defaultdict(set)
        for x, y, z in meetings:
            d[z].append([x, y])
            v[z].add(x)
            v[z].add(y)
            
        for t in sorted(d.keys()):
            uf = UnionFind(v[t])
            for x, y in d[t]:
                uf.union(x, y)
            kr = set()
            for x in v[t]:
                if x in know:
                    kr.add(uf.find(x))
            for x in v[t]:
                if uf.find(x) in kr:
                    know.add(x)
                    
        return sorted(list(know))