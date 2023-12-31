class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return math.gcd(*nums) == 1