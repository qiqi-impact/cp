class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        l = [(x, i) for (i, x) in enumerate(nums)]
        l.sort(reverse=True)
        n = len(l)
        cc = list(range(n))
        sm = nums[:]
        seen = [False] * n
        
        def find(i):
            if cc[i] != i:
                cc[i] = find(cc[i])
            return cc[i]
        
        def union(i, j):
            fi, fj = find(i), find(j)
            if fi != fj:
                cc[fi] = fj
                sm[fj] += sm[fi]
        
        ret = 0
        for x, i in l:
            seen[i] = True
            for o in [i-1, i+1]:
                if 0 <= o < n and seen[o]:
                    union(i, o)
            ret = max(ret, x * sm[find(i)])
        return ret % (10**9+7)