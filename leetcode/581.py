class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sn = sorted(nums)
        lp = 0
        for i in range(len(nums)):
            if nums[i] == sn[i]:
                lp += 1
            else:
                break
        if lp == len(nums):
            return 0
        rp = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == sn[i]:
                rp += 1
            else:
                break
        return len(nums) - lp - rp