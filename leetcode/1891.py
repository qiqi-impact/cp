class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can(x):
            ret = 0
            for r in ribbons:
                ret += r//x
                if ret >= k:
                    return True
            return False
        l, r = 0, int(1e5)
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l