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
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        dsu = DisjointSetUnion(n)
        g = [[] for _ in range(n)]
        for x, y in invocations:
            g[x].append(y)
            dsu.union(x, y)
        
        s = set([k])
        q = deque([k])
        while q:
            v = q.popleft()
            for x in g[v]:
                if x not in s:
                    s.add(x)
                    q.append(x)

        succ = len(s) == dsu.set_size(k)
        
        ret = []
        for i in range(n):
            if not succ or i not in s:
                ret.append(i)
        return ret

        