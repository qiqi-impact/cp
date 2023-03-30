class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        cur = 0
        ret = 0
        for i in range(len(prices)):
            if i == 0 or prices[i] == prices[i-1] - 1:
                cur += 1
            else:
                cur = 1
            ret += cur
        return ret