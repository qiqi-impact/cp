class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                ret += nums[i] ** 2
        return ret