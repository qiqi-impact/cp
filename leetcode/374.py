# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mi = (l+r)//2
            v = guess(mi)
            if v == 0:
                return mi
            elif v == 1:
                l = mi + 1
            else:
                r = mi - 1
        return l