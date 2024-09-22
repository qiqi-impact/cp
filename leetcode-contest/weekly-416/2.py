class Solution:
    def minNumberOfSeconds(self, m: int, w: List[int]) -> int:
        h = [(x, 1, x) for x in w]
        h.sort()
        ret = 0
        for _ in range(m):
            x, y, z = heapq.heappop(h)
            ret = x
            heapq.heappush(h, (x + (y+1)*z, y+1, z))
        return ret