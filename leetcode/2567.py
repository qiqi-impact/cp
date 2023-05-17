class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        ret = inf
        for i in range(3):
            ret = min(ret, -nums[i]+nums[len(nums)-3+i])
        return ret