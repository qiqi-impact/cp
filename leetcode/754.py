class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        cur = 0
        for i in range(1, 10**5):
            cur += i
            if cur >= target:
                if (cur - target) % 2:
                    i += 1 + i%2
                return i