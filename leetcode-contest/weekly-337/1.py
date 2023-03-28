class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ret = [0, 0]
        for i in range(32):
            if (1 << i) & n:
                ret[i%2] += 1
        return ret