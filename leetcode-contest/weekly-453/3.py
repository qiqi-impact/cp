from sortedcontainers import SortedList

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9+7
        n = len(nums)
        sl = SortedList()
        j = -1
        dp = [1]
        sdp = 1
        for i, x in enumerate(nums):
            sl.add(x)
            while sl and sl[-1] - sl[0] > k:
                j += 1
                sl.discard(nums[j])
                sdp -= dp[j]
                sdp %= MOD
            dp.append(sdp)
            sdp += dp[-1]
            sdp %= MOD
        return dp[-1]