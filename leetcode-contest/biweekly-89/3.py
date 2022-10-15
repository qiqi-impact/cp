class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can(x):
            nn = nums[:]
            for i in range(len(nn)-1, 0, -1):
                if nn[i] > x:
                    nn[i-1] += (nn[i] - x)
            if nn[0] > x:
                return False
            return True
        l, r = 0, 10**9
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi+1
        return r