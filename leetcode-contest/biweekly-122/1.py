class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        l = sorted(nums[1:])
        return nums[0] + l[0] + l[1]