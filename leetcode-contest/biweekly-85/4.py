class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
        self.val = [0] * n

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
            self.val[a] += self.val[b]

    def set_size(self, a):
        return self.size[self.find(a)]
    
    def uncover(self, idx, v):
        self.val[idx] = v
        if idx > 0 and self.val[idx-1] > 0:
            self.union(idx-1, idx)
        if idx < len(self.val)-1 and self.val[idx+1] > 0:
            self.union(idx, idx+1)
        return self.val[self.find(idx)]

    def __len__(self):
        return self.num_sets

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        dsu = DisjointSetUnion(n)
        ret = [0] * n
        mx = 0
        for i in range(n-1, 0, -1):
            mx = max(mx, dsu.uncover(removeQueries[i], nums[removeQueries[i]]))
            ret[i-1] = mx
        return ret