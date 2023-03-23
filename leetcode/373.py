class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for i, x in enumerate(nums1):
            h.append((x+nums2[0], i, 0))
        ret = []
        while len(ret) < k and h:
            x, y, z = heapq.heappop(h)
            ret.append((nums1[y], nums2[z]))
            if z != len(nums2)-1:
                heapq.heappush(h, (nums1[y]+nums2[z+1], y, z+1))
        return ret