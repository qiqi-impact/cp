class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for x, y in nums1 + nums2:
            d[x] += y
        ret = []
        for k in sorted(d.keys()):
            ret.append([k, d[k]])
        return ret