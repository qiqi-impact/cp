class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(32):
            ct = 0
            for x in nums:
                if 1 & (x >> i):
                    ct += 1
            if ct >= k:
                ret ^= (1 << i)
        return ret