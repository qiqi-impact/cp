class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dp(idx, p, left):
            if idx == len(group):
                return p >= minProfit
            ret = dp(idx+1, p, left)
            if left >= group[idx]:
                ret += dp(idx+1, min(100, p+profit[idx]), left-group[idx])
                ret %= 10**9+7
            return ret
        return int(dp(0, 0, n))