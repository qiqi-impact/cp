from sortedcontainers import SortedList

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList(range(n))
        order = list(range(n))
        order.sort(key=lambda x:nums[x])
        lst = -1
        ret = 0
        for x in order:
            cur = sl.index(x)
            if cur <= lst:
                lst -= len(sl)
            ret += cur - lst
            lst = cur - 1
            sl.discard(x)
        return ret