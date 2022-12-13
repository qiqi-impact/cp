class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def f(k):
            if k <= 1:
                return 1
            return f(k-1) + f(k-2)
        return f(n)