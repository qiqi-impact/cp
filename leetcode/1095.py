# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        L = mountain_arr.length()
        def find_peak(a, b):
            if a == b:
                return a
            c = (a+b)//2
            d = c + 1
            x, y = mountain_arr.get(c), mountain_arr.get(d)
            if x < y:
                return find_peak(d, b)
            else:
                return find_peak(a, c)
        p = find_peak(0, L-1)

        l, r = 0, p
        while l <= r:
            mi = (l+r)//2
            g = mountain_arr.get(mi)
            if g == target:
                return mi
            elif g < target:
                l = mi + 1
            else:
                r = mi - 1
        
        l, r = p, L-1
        while l <= r:
            mi = (l+r)//2
            g = mountain_arr.get(mi)
            if g == target:
                return mi
            elif g > target:
                l = mi + 1
            else:
                r = mi - 1
        
        return -1