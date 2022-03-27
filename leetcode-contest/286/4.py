class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        lp = len(piles)
        @cache
        def dp(idx, left):
            if idx == lp:
                return 0
            ret = dp(idx+1, left)
            cur = 0
            for i in range(min(left, len(piles[idx]))):
                cur += piles[idx][i]
                ret = max(ret, cur + dp(idx+1, left-i-1))
            return ret
        return dp(0, k)