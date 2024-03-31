class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        l = sum([int(t) for t in str(x)])
        if x % l == 0:
            return l
        return -1