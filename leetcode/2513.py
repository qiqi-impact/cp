class Solution:
    def minimizeSet(self, d1: int, d2: int, u1: int, u2: int) -> int:
        lcm = math.lcm(d1, d2)
        def can(x):
            f1 = x // d2 - x // lcm
            f2 = x // d1 - x // lcm
            left = max(u1 - f1, 0) + max(u2 - f2, 0)
            wc = x - x // d1 - x // d2 + x // lcm
            return wc >= left
        l, r = 0, 10**10
        while l < r:
            mi = (l+r)//2
            if can(mi):
                r = mi
            else:
                l = mi + 1
        return r