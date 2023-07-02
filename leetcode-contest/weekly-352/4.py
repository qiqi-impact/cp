from sortedcontainers import SortedList

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            sl = SortedList([nums[i]])
            cur = 0
            for j in range(i-1, -1, -1):
                idx = sl.bisect_left(nums[j])
                sl.add(nums[j])
                if 0 <= idx-1 and sl[idx] - sl[idx-1] > 1:
                    cur += 1
                if idx+1 < len(sl) and sl[idx+1] - sl[idx] > 1:
                    cur += 1
                if 1 <= idx <= len(sl)-2 and sl[idx+1] - sl[idx-1] > 1:
                    cur -= 1
                ret += cur
        return ret