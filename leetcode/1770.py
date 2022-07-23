class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        mx = -float('inf')
        dp = [float('-inf')] * m
        for i in range(m+1):
            ndp = [float('-inf')] * (m+1)
            if i == 0: ndp[0] = 0
            for j in range(m-i+1):
                if i > 0:
                    ndp[j] = max(ndp[j], dp[j] + nums[i-1]*multipliers[i+j-1])
                if j > 0:
                    ndp[j] = max(ndp[j], ndp[j-1] + nums[-j]*multipliers[i+j-1])
                if i+j==m: mx = max(mx, ndp[j])
            dp = ndp
        return mx