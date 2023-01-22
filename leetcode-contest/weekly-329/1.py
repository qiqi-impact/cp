class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ret = 0
        for i, x in enumerate(str(n)):
            m = 1 if i%2 == 0 else -1
            ret += m * int(x)
        return ret