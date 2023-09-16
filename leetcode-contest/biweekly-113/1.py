class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sn = sorted(nums)
        for i in range(101):
            if sn == nums:
                return i
            nums = [nums[-1]] + nums[:-1]
        return -1