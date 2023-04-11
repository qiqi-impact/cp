class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        ret = 0
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                t = math.sqrt(nums2[i] * nums2[j])
                l = bisect.bisect_left(nums1, t)
                r = bisect.bisect_right(nums1, t)
                ret += r - l

        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                t = math.sqrt(nums1[i] * nums1[j])
                l = bisect.bisect_left(nums2, t)
                r = bisect.bisect_right(nums2, t)
                ret += r - l
        return ret