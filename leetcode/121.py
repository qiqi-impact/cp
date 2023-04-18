class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        mn = inf
        for x in prices:
            mn = min(mn, x)
            ret = max(ret, x - mn)
        return ret