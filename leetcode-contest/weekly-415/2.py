class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        b1, b2, b3, b4 = -inf, -inf, -inf, -inf
        for x in b:
            b4 = max(b4, b3 + x * a[3])
            b3 = max(b3, b2 + x * a[2])
            b2 = max(b2, b1 + x * a[1])
            b1 = max(b1, x * a[0])
        return b4
