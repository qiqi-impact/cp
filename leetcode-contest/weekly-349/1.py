class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for x in nums:
            if x != min(nums) and x != max(nums):
                return x
        return -1