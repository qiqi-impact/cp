class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        ret = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= 2 * k:
                j += 1
                ret = max(ret, j - i)
        return ret