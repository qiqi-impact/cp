class Solution:
    def countDigitOne(self, n: int) -> int:
        m = 1
        ret = 0
        tail = 0
        while n:
            nn, md = n // 10, n % 10
            ret += nn * m
            if md > 1:
                ret += m
            elif md == 1:
                ret += tail+1
            tail += m * md
            m *= 10
            n = nn
        return ret