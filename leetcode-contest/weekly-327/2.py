class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ret = 0
        h = []
        for x in nums:
            heapq.heappush(h, -x)
        for i in range(k):
            cur = heapq.heappop(h)
            cur = -cur
            ret += cur
            cur = (cur + 2) // 3
            heapq.heappush(h, -cur)
        return ret