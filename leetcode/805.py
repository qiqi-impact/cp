class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        A = sum(nums)

        d = defaultdict(set)
        d[0].add(0)
        for i in range(n//2):
            v = nums[i]
            nd = defaultdict(set)
            for k in d:
                for t in d[k]:
                    nd[k].add(t)
                    nd[k+1].add(t+v)
            d = nd

        e = defaultdict(set)
        e[0].add(0)
        for i in range(n//2, n):
            v = nums[i]
            ne = defaultdict(set)
            for k in e:
                for t in e[k]:
                    ne[k].add(t)
                    ne[k+1].add(t+v)
            e = ne

        for k in d:
            for l in e:
                if k+l == 0 or k+l == n:
                    continue
                for s in d[k]:
                    if (k + l) * A % n == 0 and A * (k + l) // n - s in e[l]:
                        return True
        return False
        