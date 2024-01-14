class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def can(t):
            q = 0
            for i in range(x, 128+x, x):
                p = 1 << (i-1)
                q += (t//(p*2))*p + max(0, t%(p*2) - p)
                if q > k:
                    return False
            return True
        
        l, r = 0, 10**20
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l-1