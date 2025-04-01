from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        cost = []
        n = len(nums)

        sl = SortedList()
        for i in range(x):
            sl.add(nums[i])
        med = sl[x//2]

        cur = 0
        for i in range(x):
            cur += abs(nums[i] - med)
        cost.append(cur)

        for i in range(x, n):
            cur -= abs(nums[i-x] - med)
            cur += abs(nums[i] - med)
            sl.discard(nums[i-x])
            sl.add(nums[i])
            nmed = sl[x//2]
            # print(i, med, nmed, cur)
            if med == nmed:
                pass
            elif med < nmed:
                idx = sl.bisect_left(nmed)
                cur -= (x - idx) * (nmed - med)
                idx = sl.bisect_right(med)
                cur += (idx) * (nmed - med)
            else:
                idx = sl.bisect_left(med)
                cur += (x - idx) * (med - nmed)
                idx = sl.bisect_right(nmed)
                cur -= (idx) * (med - nmed)
            med = nmed
            cost.append(cur)

        dp = [[inf for _ in range(k+1)] for _ in range(n+1)]
        dp[n][k] = 0
        for i in range(n-1, -1, -1):
            for j in range(k+1):
                dp[i][j] = dp[i+1][j]
                if i + x <= n and j < k:
                    dp[i][j] = min(dp[i][j], cost[i] + dp[i+x][j+1])
        return dp[0][0]