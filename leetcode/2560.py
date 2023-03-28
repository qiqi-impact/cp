class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can(x):
            skip = False
            amt = 0
            for i in range(len(nums)):
                if skip:
                    skip = False
                    continue
                if nums[i] <= x:
                    amt += 1
                    skip = True
                    if amt >= k:
                        return True
            return False
        l, r = 0, max(nums)
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r