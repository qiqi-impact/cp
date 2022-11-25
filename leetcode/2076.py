class DisjointSetUnion:
    def __init__(self, n, hate):
        self.parent = list(range(n))
        self.size = [1] * n
        self.hate = hate
        self.contains = [set([i]) for i in range(n)]
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
            for h in self.hate[a]:
                if h in self.contains[b]:
                    return False
                
            for h in self.hate[b]:
                if h in self.contains[a]:
                    return False
            
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]
            
            self.hate[a] |= self.hate[b]
            self.contains[a] |= self.contains[b]
            return True
        return True

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        hate = [set() for _ in range(n)]
        for x, y in restrictions:
            hate[x].add(y)
            hate[y].add(x)
        dsu = DisjointSetUnion(n, hate)
        ret = []
        for x, y in requests:
            ret.append(dsu.union(x, y))
        return ret
        
        
        
        
        