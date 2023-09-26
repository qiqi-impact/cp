from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        l = nums[:]
        for i in range(len(l)):
            if l[i]%2:
                l[i] *= 2
        l.sort()
        mxv = l[0]
        for i in range(len(l)):
            while l[i]%2==0:
                l[i] //= 2
        sl = SortedList()
        for i, x in enumerate(l):
            sl.add((x, i))
        ret = inf
        while 1:
            ret = min(ret, sl[-1][0] - sl[0][0])
            x, y = sl.pop(0)
            if y == 0 and x == mxv:
                break
            sl.add((2*x, y))
        return ret