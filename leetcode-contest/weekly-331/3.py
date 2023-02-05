class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can(x):
            dp = [0] * (len(nums)+2)            
            for i in range(len(nums)-1, -1, -1):
                dp[i] = dp[i+1]
                if nums[i] <= x:
                    dp[i] = max(dp[i], 1 + dp[i+2])
                if dp[i] >= k:
                    return True
            return False
        l, r = 0, max(nums)
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi+1
        return l