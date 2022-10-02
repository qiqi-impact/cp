class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        a = bin(num1).count('1')
        b = bin(num2).count('1')
        if a == b:
            return num1
        elif b < a:
            ret = 0
            for i in range(31, -1, -1):
                if 1 & (num1 >> i):
                    ret ^= (1 << i)
                    b -= 1
                    if b == 0:
                        return ret
        else:
            ret = num1
            for i in range(32):
                if not (1 & (num1 >> i)):
                    ret ^= (1 << i)
                    b -= 1
                    if b == a:
                        return ret