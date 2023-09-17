class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        if nums[0] != 0:
            ret += 1
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i+1] <= i+1:
                continue
            if nums[i] < i+1:
                ret += 1
        return ret