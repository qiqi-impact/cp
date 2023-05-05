class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        on = n
        m = 10
        while sum([int(x) for x in str(n)]) > target:
            n = (n//m)*m
            n += m
            while n%m == 0:
                m *= 10
        return n - on