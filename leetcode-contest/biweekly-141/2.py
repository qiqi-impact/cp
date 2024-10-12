class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ret = []
        for x in nums:
            if x == 2:
                ret.append(-1)
                continue
            for i in range(33):
                if not (x & 1 << i):
                    x ^= 1 << (i - 1)
                    ret.append(x)
                    break
        return ret