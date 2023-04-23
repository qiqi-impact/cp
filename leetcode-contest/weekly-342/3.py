from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        sl = SortedList()
        ret = []
        for i in range(k):
            sl.add(nums[i])
        ret.append(min(0, sl[x-1]))
        for i in range(k, len(nums)):
            sl.add(nums[i])
            sl.discard(nums[i-k])
            ret.append(min(0, sl[x-1]))
        return ret