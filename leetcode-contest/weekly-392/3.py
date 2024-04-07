class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = 0
        m = len(nums)//2
        for i, x in enumerate(nums):
            if i < m and nums[i] > k:
                ret += nums[i] - k
            if i == m and nums[i] != k:
                ret += abs(nums[i] - k)
            if i > m and nums[i] < k:
                ret += k - nums[i]
        return ret