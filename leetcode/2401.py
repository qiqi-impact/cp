class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        j = 0
        ret = 0
        win = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] & win == 0:
                win += nums[j]
                j += 1
                ret = max(ret, j - i)
            win -= nums[i]
        return ret