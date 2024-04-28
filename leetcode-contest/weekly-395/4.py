class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        cap = n * (n+1) // 2
        def can(x):
            j = 0
            f = {}
            r = 0
            for i in range(n):
                while j != n:
                    if len(f) == x and nums[j] not in f:
                        break
                    f[nums[j]] = f.get(nums[j], 0) + 1
                    j += 1
                r += j - i
                v = nums[i]
                f[v] -= 1
                if f[v] == 0:
                    del f[v]
            if r >= (1+cap) // 2:
                return True
            return False
        
        l, r = 1, n
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r