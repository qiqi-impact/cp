class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        ret = 0
        ct = 1
        for i in range(1, n):
            if ct >= 1 and weight[i] < weight[i-1]:
                ret += 1
                ct = 0
            else:
                ct += 1
        return ret