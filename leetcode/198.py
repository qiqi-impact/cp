class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(idx):
            if idx >= len(nums):
                return 0
            return max(dp(idx+1), nums[idx] + dp(idx+2))
        return dp(0)