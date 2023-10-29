class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dp(idx, lag):
            if idx == n:
                return 0
            if nums[idx] >= k:
                return dp(idx+1, 0)
            ret = inf
            if lag < 2:
                ret = min(ret, dp(idx+1, lag + 1))
            ret = min(ret, k - nums[idx] + dp(idx+1, 0))
            return ret
        return dp(0, 0)