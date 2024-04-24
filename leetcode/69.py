class Solution:
    def mySqrt(self, x: int) -> int:
        def pred(t):
            return t*t <= x
        
        l, r = 0, 2**30
        while l < r:
            mi = (l+r+1)//2
            if pred(mi):
                l = mi
            else:
                r = mi - 1
        return l