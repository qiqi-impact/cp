class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        l = list(zip(nums1, nums2))
        l.sort(key=lambda x:-x[1])

        h = []
        sm = 0
        for i in range(k):
            heapq.heappush(h, l[i][0])
            sm += l[i][0]
        ret = sm * l[k-1][1]

        for i in range(k, len(l)):
            heapq.heappush(h, l[i][0])
            sm += l[i][0]
            sm -= heapq.heappop(h)
            ret = max(ret, sm * l[i][1])

        return ret