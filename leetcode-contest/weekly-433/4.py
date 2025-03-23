MOD = 10**9+7

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.bounds = [[i, i] for i in range(n)]
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
            self.bounds[a][0] = min(self.bounds[a][0], self.bounds[b][0])
            self.bounds[a][1] = max(self.bounds[a][1], self.bounds[b][1])

    def set_size(self, a):
        return self.size[self.find(a)]

    def set_bounds(self, a):
        return self.bounds[self.find(a)]

    def __len__(self):
        return self.num_sets

class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        n = len(nums)
        def g(l):
            nonlocal ret, n
            dsu = DisjointSetUnion(n)
            ok = set()
            for x, i in l:
                ok.add(i)
                for j in [i-1, i+1]:
                    if 0 <= j < len(nums) and j in ok:
                        dsu.union(i, j)
                a, b = dsu.set_bounds(i)
                aa, bb = i - a, b - i
                f = min(k, aa + bb + 1)
                r = (f) * (f + 1) // 2
                if aa < f - 1:
                    q = f - 1 - aa
                    r -= q * (q + 1) // 2
                if bb < f - 1:
                    q = f - 1 - bb
                    r -= q * (q + 1) // 2
                ret += r * x

        l = [(x, i) for (i, x) in enumerate(nums)]
        l.sort()
        g(l)
        l.sort(reverse=True)
        g(l)
        return ret
        