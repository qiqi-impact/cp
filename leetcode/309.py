# algo by betsymp

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, sold_last = -inf, 0, 0
        for p in prices:
            temp = hold
            hold = max(hold, sold - p)
            sold = sold_last
            sold_last = max(sold_last, temp + p)
        return sold_last