class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur = 0
        d = 1
        for i in range(time):
            if cur == 0 and d == -1:
                d = 1
            elif cur == n-1 and d == 1:
                d = -1
            cur += d
        return cur + 1