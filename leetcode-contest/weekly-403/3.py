class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        ret = [nums[0], -inf]
        for i in range(1, len(nums)):
            a = max(ret) + nums[i]
            b = ret[0] - nums[i]
            ret = [a, b]
        return max(ret)