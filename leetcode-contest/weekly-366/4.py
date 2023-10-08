class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        ct = [0] * 32
        for x in nums:
            for i in range(32):
                if 1 & (x >> i):
                    ct[i] += 1
        ret = 0
        for i in range(k):
            cur = 0
            for j in range(32):
                if ct[j]:
                    ct[j] -= 1
                    cur += (1 << j)
            ret += (cur * cur)
            ret %= 10**9+7
        return ret