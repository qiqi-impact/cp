class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def single_is_on_left(x):
            if x == len(nums)-1:
                return True
            return nums[x] != nums[x+1]
        l, r = 0, (len(nums)-1)//2
        while l < r:
            mi = (l+r)//2
            if single_is_on_left(2*mi):
                r = mi
            else:
                l = mi + 1
        return nums[2*r]