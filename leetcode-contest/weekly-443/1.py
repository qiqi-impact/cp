class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ret = []
        mn = inf
        for x in cost:
            mn = min(mn, x)
            ret.append(mn)
        return ret