class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(idx, k):
            if idx == len(piles):
                return 0 if k == 0 else -inf
            cur = 0
            ret = dp(idx+1, k)
            for x in piles[idx]:
                k -= 1
                cur += x
                ret = max(ret, cur+dp(idx+1, k))
                if k == 0:
                    break
            return ret
        return dp(0, k)