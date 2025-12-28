class Solution:
    def minimumCost(self, a: int, b: int, c: int, n1: int, n2: int) -> int:
        if c <= min(a, b):
            return c * max(n1, n2)
        if c > a + b:
            return a * n1 + b * n2
        return c * min(n1, n2) + min(a, c) * (n1 - min(n1, n2)) + min(b, c) * (n2 - min(n1, n2))