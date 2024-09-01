class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        h = []
        ret = []
        for x, y in queries:
            v = abs(x) + abs(y)
            heapq.heappush(h, -v)
            if len(h) > k:
                heapq.heappop(h)
            if len(h) == k:
                ret.append(-h[0])
            else:
                ret.append(-1)
        return ret