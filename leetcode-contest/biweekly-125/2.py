class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h = []
        for x in nums:
            heapq.heappush(h, x)
        ct = 0
        while h[0] < k:
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            heapq.heappush(h, x*2 + y)
            ct += 1
        return ct