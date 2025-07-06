from sortedcontainers import SortedList

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
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu = DisjointSetUnion(c)
        for x, y in connections:
            x -= 1
            y -= 1
            dsu.union(x, y)
        online = [1] * c
        grids = defaultdict(SortedList)
        for i in range(c):
            grids[dsu.find(i)].add(i)

        ret = []
        for t, x in queries:
            # print(grids)
            x -= 1
            if t == 2:
                if online[x]:
                    online[x] = 0
                    grids[dsu.find(x)].discard(x)
            else:
                if online[x]:
                    ret.append(x+1)
                else:
                    w = grids[dsu.find(x)]
                    ret.append((w[0]+1) if w else -1)
        return ret
        


        