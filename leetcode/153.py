class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        l, r = 0, len(nums)-1
        while l < r-1:
            mi = (l+r)//2
            if nums[mi] > nums[l]:
                l = mi
            else:
                r = mi
        return min(nums[l:r+1])