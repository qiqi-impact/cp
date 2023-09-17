class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ret = 0
        for i, x in enumerate(nums):
            if i.bit_count() == k:
                ret += x
        return ret