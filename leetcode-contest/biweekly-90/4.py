from sortedcontainers import SortedList

class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = sorted([(x, i) for (i, x) in enumerate(nums)], key=lambda y:(y[0], -y[1]))
        
        p = [-1] * n
        sl = SortedList()
        for i in range(n-1, -1, -1):
            b = l[i][1]
            idx = sl.bisect(b)
            if idx < len(sl)-1:
                p[i] = nums[sl[idx+1]]
            sl.add(b)
        
        ret = [None] * n
        for i in range(n):
            ret[l[i][1]] = p[i]
        return ret