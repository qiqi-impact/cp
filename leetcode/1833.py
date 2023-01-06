class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:    
        costs.sort()
        ret = 0
        for c in costs:
            if c <= coins:
                coins -= c
                ret += 1
            else:
                break
        return ret