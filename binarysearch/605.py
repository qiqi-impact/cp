class Solution:
    def solve(self, nums):
        sm = sum(nums)
        if sm%2 == 1:
            return False
        tgt = sm//2

        @cache
        def dp(idx, sofar):
            nonlocal tgt
            if idx == len(nums):
                return (sofar == tgt)
            if dp(idx+1, sofar):
                return True
            if nums[idx] + sofar <= tgt:
                return dp(idx+1, sofar + nums[idx])
            return False

        return dp(0, 0)