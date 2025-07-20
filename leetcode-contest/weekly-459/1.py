class Solution:
    def checkDivisibility(self, n: int) -> bool:
        l = [int(c) for c in str(n)]
        m = 1
        for x in l:
            m *= x
        return n % (sum(l) + m) == 0