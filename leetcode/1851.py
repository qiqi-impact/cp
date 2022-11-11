class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        h = []
        intervals.sort()
        sq = sorted(queries)
        ans = {}
        p = 0
        for q in sq:
            while p < len(intervals) and intervals[p][0] <= q:
                heapq.heappush(h, (intervals[p][1] - intervals[p][0] + 1, intervals[p][1]))
                p += 1
            while h and h[0][1] < q:
                heapq.heappop(h)
            ans[q] = -1
            if h:
                ans[q] = h[0][0]
        return [ans[q] for q in queries]