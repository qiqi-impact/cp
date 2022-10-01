class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = len(nums1), len(nums2)
        ret = 0
        if a%2 == 1:
            for x in nums2:
                ret ^= x
        if b%2 == 1:
            for x in nums1:
                ret ^= x
        return ret