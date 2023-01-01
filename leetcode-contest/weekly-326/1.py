class Solution:
    def countDigits(self, num: int) -> int:
        l = [int(x) for x in str(num)]
        ret = 0
        for x in l:
            if num%x == 0:
                ret += 1
        return ret