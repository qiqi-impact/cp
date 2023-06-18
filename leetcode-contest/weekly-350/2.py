class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ret = inf
        for i in range(len(nums)-1):
            ret = min(ret, nums[i+1] - nums[i])
        return ret