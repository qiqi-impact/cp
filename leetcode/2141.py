class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        
        def can(x):
            idx = bisect.bisect_left(batteries, x)  
            filled = len(batteries) - idx
            cur = 0
            for i in range(idx):
                cur += batteries[i]
                if cur >= x:
                    cur -= x
                    filled += 1
                if filled >= n:
                    return True
            return False
        
        l, r = min(batteries), sum(batteries)//n
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l