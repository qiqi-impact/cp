class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        inc = [len(nums)-1]
        dec = [len(nums)-1] # no equal
        dp = [float('inf')] * len(nums)
        dp[-1] = costs[-1]
        for i in range(len(nums)-2, -1, -1):
            while inc and nums[i] <= nums[inc[-1]]:
                inc.pop()
            while dec and nums[i] > nums[dec[-1]]:
                dec.pop()
            dp[i] = dp[i+1] + costs[i]
            if inc:
                dp[i] = min(dp[i], costs[i] + dp[inc[-1]])
            if dec:
                dp[i] = min(dp[i], costs[i] + dp[dec[-1]])
            inc.append(i)
            dec.append(i)
        return dp[0] - costs[0]