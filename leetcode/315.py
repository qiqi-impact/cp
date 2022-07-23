from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        ret = [None] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            idx = sl.bisect_left(nums[i])
            ret[i] = idx
            sl.add(nums[i])
        return ret