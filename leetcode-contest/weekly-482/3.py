class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        if k % 5 == 0:
            return -1
        cur = 0
        for i in range(2*k+1):
            cur += pow(10, i, k)
            cur %= k
            if cur == 0:
                return i + 1
        return -1