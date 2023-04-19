class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mx = -1
        BIGINT = 1 << 30
        for i in range(len(nums)):
            if not 1 <= nums[i] <= 10**5:
                nums[i] = 0
        for i in range(len(nums)):
            v = nums[i] % BIGINT
            if 1 <= v < len(nums):
                nums[v] += BIGINT
            mx = max(mx, v)
        for i in range(1, len(nums)):
            if nums[i] < BIGINT:
                return i
        if mx == len(nums):
            return len(nums)+1
        return len(nums)

    