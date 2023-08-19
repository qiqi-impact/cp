class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        @cache
        def dp(idx, k):
            if idx == len(nums):
                return 0
            v = nums[idx]
            ret = inf
            if v >= k:
                ret = dp(idx+1, v)
            ret = min(ret, 1 + dp(idx+1, k))
            return ret
        return dp(0, 1)