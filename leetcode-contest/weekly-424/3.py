class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def can(t):
            ls = [0] * (n+1)
            for i in range(t):
                x, y, z = queries[i]
                ls[x] += z
                ls[y+1] -= z
            cur = 0
            for i in range(n):
                cur += ls[i]
                if cur < nums[i]:
                    return False
            return True
        if not can(len(queries)):
            return -1
        l, r = 0, len(queries)
        while l < r:
            mi = (l + r) // 2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r