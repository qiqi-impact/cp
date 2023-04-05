class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ret = 0
        cur = 0
        for i in range(len(cost)-1, -1, -1):
            if cur == 2:
                cur = 0
            else:
                cur += 1
                ret += cost[i]
        return ret