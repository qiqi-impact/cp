class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        a, b, c = s1[0], s2[0], s3[0]
        sl = len(s1) + len(s2) + len(s3)
        ml = min(len(s1), len(s2), len(s3))
        if a != b or a != c:
            return -1
        for i in range(1, ml):
            a += s1[i]
            b += s2[i]
            c += s3[i]
            if a != b or a != c:
                return sl - 3 * i
        return sl - 3 * ml