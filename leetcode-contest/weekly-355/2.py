class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ret = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= nums[i+1]:
                nums[i] += nums[i+1]
            ret = max(ret, nums[i])
        return ret