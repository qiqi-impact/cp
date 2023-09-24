class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x = s.count('1')
        ret = ('1' * (x-1)) + ('0' * (len(s) - (x-1) - 1)) + '1'
        return ret