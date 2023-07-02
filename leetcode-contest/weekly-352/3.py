from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = sorted(zip(nums, range(len(nums))))
        sl = SortedList(range(-1, len(nums)+1))
        ret = 0
        h = []
        for x, i in l:
            while h and h[0][0] < x-2:
                sl.add(h[0][1])
                heapq.heappop(h)
            idx = sl.index(i)
            ret += (sl[idx] - sl[idx-1]) * (sl[idx+1] - sl[idx])
            heapq.heappush(h, (x, i))
            sl.remove(i)
        return ret