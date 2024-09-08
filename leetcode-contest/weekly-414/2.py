class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        def can(x):
            cur = -10**18
            for t in start:
                nx = cur + x
                if nx > t + d:
                    return False
                cur = max(t, nx)
            return True

        l, r = 0, 10**18
        while l < r:
            mi = (l+r+1)//2
            if can(mi):
                l = mi
            else:
                r = mi - 1
        return l