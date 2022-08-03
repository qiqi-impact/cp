class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        times = sorted(list(set(startTime) | set(endTime)))
        m = {times[i]:i for i in range(len(times))}
        startTime = [m[x] for x in startTime]
        endTime = [m[x] for x in endTime]
        dp = [None] * (len(times)+1)
        dp[0] = 0
        tt = sorted(list(zip(startTime, endTime, profit)), key=lambda x:x[1])
        ttp = 0
        for i in range(1, len(dp)):
            dp[i] = dp[i-1]
            while ttp < len(tt) and tt[ttp][1] <= i:
                dp[i] = max(dp[i], tt[ttp][2] + dp[tt[ttp][0]])
                ttp += 1
        return dp[-1]