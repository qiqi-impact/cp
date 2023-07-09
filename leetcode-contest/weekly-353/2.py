class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(idx):
            if idx == n-1:
                return 0
            ret = -inf
            for i in range(idx+1, n):
                if abs(nums[i] - nums[idx]) <= target:
                    ret = max(ret, 1 + dp(i))
            return ret
        ret = dp(0)
        return ret if ret != -inf else -1