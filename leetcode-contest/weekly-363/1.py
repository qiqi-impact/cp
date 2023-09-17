class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ret = 0
        for i, x in enumerate(nums):
            if bin(i).count('1') == k:
                ret += x
        return ret