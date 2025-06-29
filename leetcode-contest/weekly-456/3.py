class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dp(idx, left):
            if idx == n:
                return 0 if left == 0 else inf
            if left == 0:
                return inf
            cur = 0
            ret = inf
            for j in range(idx + 1, n + 2 - left):
                cur ^= nums[j - 1]
                ret = min(ret, max(cur, dp(j, left - 1)))
            return ret
        return dp(0, k)