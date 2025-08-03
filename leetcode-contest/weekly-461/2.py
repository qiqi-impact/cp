class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        ret = 0
        ct = True
        for i in range(1, n):
            if ct and weight[i] < weight[i-1]:
                ret += 1
                ct = False
            else:
                ct = True
        return ret