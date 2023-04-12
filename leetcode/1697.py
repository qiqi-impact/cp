class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        
        edgeList.sort(key=lambda x:x[2])
        ep = 0
        ans = {}
        
        q = sorted(queries, key=lambda x:x[2])
        
        for x, y, z in q:
            while ep < len(edgeList) and edgeList[ep][2] < z:
                uf.union(edgeList[ep][0], edgeList[ep][1])
                ep += 1
            ans[(x, y, z)] = uf.find(x) == uf.find(y)
        
        return [ans[tuple(x)] for x in queries]
        