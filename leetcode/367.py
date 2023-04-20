class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def lte(x):
            return x*x <= num
        l, r = 1, num
        while l < r:
            mi = (l+r+1)//2
            if lte(mi):
                l = mi
            else:
                r = mi - 1
        return l*l == num