class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        mx = 0
        coins.sort()
        for x in coins:
            if x > mx + 1:
                return mx + 1
            mx += x
        return mx + 1