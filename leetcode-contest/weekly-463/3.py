class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        s = [-inf] * k
        s[0] = 0
        n = len(nums)
        dp = [0] * (n + 1)
        pf = [0]
        for i in range(n):
            pf.append(pf[-1] + nums[i])
        for i in range(1, n + 1):
            cur = pf[i]
            dp[i] = max(dp[i-1], cur + s[cur%k])
            s[cur%k] = max(s[cur%k], dp[i] - pf[i])
        return sum(nums) - dp[n]