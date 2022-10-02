class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ret = 0
        for i in range(1, 1001):
            if a%i == 0 and b%i == 0:
                ret += 1
        return ret