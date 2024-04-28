class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        a, b, c = nums1[:3]
        for x in c, b, a:
            d = nums2[0] - x
            bp = 0
            skip = 0
            for y in nums1:
                if bp == len(nums2) or nums2[bp] != y + d:
                    skip += 1
                    if skip > 2:
                        break
                else:
                    bp += 1
            if skip == 2:
                return d