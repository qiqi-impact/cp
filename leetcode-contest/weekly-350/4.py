class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dp(idx, left):
            if left == 0:
                return 0
            if idx == len(cost):
                return inf
            ret = min(dp(idx+1, left), cost[idx] + dp(idx+1, max(0, left-time[idx]-1)))
            return ret
        return dp(0, len(cost))