class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        @cache
        def dp(idx, a, b):
            if a < b:
                return dp(idx, b, a)
            if a == 0 and b == 0:
                return pow(2, n - idx, MOD)
            if idx == n:
                return 0
            return (dp(idx+1, max(0, a-nums[idx]), b) + dp(idx+1, a, max(b-nums[idx], 0))) % MOD
        return dp(0, k, k)