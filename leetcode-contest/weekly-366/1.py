class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ret = 0
        for x in range(1, n+1):
            if x%m == 0:
                ret -= x
            else:
                ret += x
        return ret