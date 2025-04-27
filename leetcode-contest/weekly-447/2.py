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
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        nums = [(x, i) for (i, x) in enumerate(nums)]
        nums.sort()

        m = {}
        for i in range(n):
            m[nums[i][1]] = i
        
        dsu = DisjointSetUnion(n)
        for i in range(n-1):
            if abs(nums[i][0] - nums[i+1][0]) <= maxDiff:
                dsu.union(i, i+1)
        
        ret = []
        for x, y in queries:
            ret.append(dsu.find(m[x]) == dsu.find(m[y]))
        return ret
        
        