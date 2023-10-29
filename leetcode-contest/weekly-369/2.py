class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        tot = [0, 0]
        lz, rz = 0, 0
        for x in nums1:
            if x == 0:
                lz += 1
                tot[0] += 1
            else:
                tot[0] += x
        for x in nums2:
            if x == 0:
                rz += 1
                tot[1] += 1
            else:
                tot[1] += x
        if tot[0] == tot[1]:
            return tot[0]
        elif tot[0] > tot[1]:
            if rz == 0:
                return -1
            else:
                return tot[0]
        else:
            if lz == 0:
                return -1
            else:
                return tot[1]