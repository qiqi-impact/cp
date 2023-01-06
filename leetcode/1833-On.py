class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:    
        amt = [0] * (10**5+1)
        for c in costs:
            amt[c] += 1
        ret = 0
        for c in range(len(amt)):
            v = amt[c]
            if c * v <= coins:
                coins -= c * v
                ret += v
            else:
                ret += coins // c
                break
        return ret