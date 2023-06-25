class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 1000):
            num1 -= num2
            if num1 > 0:
                s = bin(num1).count('1')
                if s <= i and num1 >= i:
                    return i
        return -1