from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        mn = 0
        for i in range(k):
            mn += nums[i]
            
        l, r = SortedList(), SortedList()
        
        hs = 0
        pt = 2
        
        for i in range(1, len(nums)):
            p = (nums[i], i)
            if l.count(p):
                l.discard(p)
                hs -= nums[i]
            if r.count(p):
                r.discard(p)
            while pt <= i+dist and pt < len(nums):
                np = (nums[pt], pt)
                r.add(np)
                pt += 1
            while r and len(l) < k-2:
                q = r.pop(0)
                l.add(q)
                hs += q[0]
            while l and r and l[-1][0] > r[0][0]:
                x, y = l.pop(-1), r.pop(0)
                l.add(y)
                r.add(x)
                hs += y[0] - x[0]
            if len(l) == k-2:
                mn = min(mn, hs + nums[0] + nums[i])
        return mn