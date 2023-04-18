class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        j = 0
        h = []
        sm = 0
        ret = 0
        for i in range(n):
            while j < n:
                heapq.heappush(h, (-chargeTimes[j], j))
                sm += runningCosts[j]
                j += 1
                if (j - i) * sm - h[0][0] <= budget:
                    ret = max(ret, j - i)
                else:
                    break
            sm -= runningCosts[i]
            while h and h[0][1] <= i:
                heapq.heappop(h)
        return ret
