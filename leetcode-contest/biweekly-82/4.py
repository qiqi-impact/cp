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
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        
        for x in nums:
            if x > threshold:
                return 1
        
        dsu = DisjointSetUnion(n)
        seen = [False] * n
        
        l = []
        for i in range(n):
            l.append(threshold // nums[i])
            if l[-1] * nums[i] <= threshold:
                l[-1] += 1
        
        o = [(l[i], i) for i in range(n)]
        o.sort()
        for x, y in o:
            seen[y] = True
            for k in [y-1, y+1]:
                if 0 <= k < n and seen[k]:
                    dsu.union(y, k)
                    ss = dsu.set_size(y)
                    if ss >= x:
                        return ss
        return -1                        
            
        
        