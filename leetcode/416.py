class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tgt = sum(nums)
        if tgt % 2 == 1:
            return False
        tgt //= 2
        @cache
        def dp(idx, sm):
            if idx == len(nums):
                return sm == tgt
            if dp(idx+1, sm):
                return True
            if nums[idx] + sm <= tgt and dp(idx+1, nums[idx] + sm):
                return True
            return False
        return dp(0, 0)