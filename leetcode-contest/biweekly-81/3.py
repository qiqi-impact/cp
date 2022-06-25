class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ret = 0
        for n in nums:
            ret |= n
        return ret