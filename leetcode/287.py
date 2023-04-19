class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def can(x):
            ret = 0
            for n in nums:
                if n <= x:
                    ret += 1
                    if ret > x:
                        return True
            return False
        l, r = 1, len(nums)-1
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r