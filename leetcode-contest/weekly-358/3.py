from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        ret = inf
        sl = SortedList()
        for i in range(len(nums)):
            idx = sl.bisect_left(nums[i])
            if idx < len(sl):
                ret = min(ret, sl[idx] - nums[i])
            if idx > 0:
                ret = min(ret, nums[i] - sl[idx-1])
            if i >= x-1:
                sl.add(nums[i-(x-1)])
        return ret