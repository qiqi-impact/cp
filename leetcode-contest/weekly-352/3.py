from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        sl = SortedList()
        j = 0
        ret = 0
        for i in range(len(nums)):
            sl.add(nums[i])
            while sl[-1] - sl[0] > 2:
                sl.remove(nums[j])
                j += 1
            ret += i-j+1
        return ret