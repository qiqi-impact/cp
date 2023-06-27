class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ret = []
        h = [(nums1[0]+nums2[0], 0, 0)]
        for _ in range(k):
            if not h: break
            _, i, j = heapq.heappop(h)
            ret.append((nums1[i], nums2[j]))
            if j == 0 and i != len(nums1)-1:
                heapq.heappush(h, (nums1[i+1]+nums2[j], i+1, j))
            if j != len(nums2)-1:
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))
        return ret