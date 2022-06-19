class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0: return 0
        s = 0
        for i in range(10):
            s += k
            if s % 10 == num % 10:
                if s > num:
                    return -1
                return i+1
        return -1