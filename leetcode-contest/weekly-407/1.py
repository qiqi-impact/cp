class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ret = 0
        for i in range(32):
            a = n & 1 << i
            b = k & 1 << i
            if a and not b:
                ret += 1
            if b and not a:
                return -1
        return ret