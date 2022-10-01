from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        a = [nums1[i] - nums2[i] for i in range(len(nums1))]
        sl = SortedList()
        ret = 0
        for x in a:
            idx = sl.bisect(x + diff)
            ret += idx
            sl.add(x)
        return ret