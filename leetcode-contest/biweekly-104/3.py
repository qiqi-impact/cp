class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        freq = [0] * 32
        for i in range(32):
            for x in nums:
                if (1 << i) & x:
                    freq[i] += 1
        base = 0
        for i in range(32):
            if freq[i]:
                base ^= (1 << i)
                
        ret = 0
        for i in range(len(nums)):
            x = nums[i]
            bb = base
            for j in range(32):
                if freq[j] == 1 and ((1 << j) & x):
                    bb ^= (1 << j)
            ret = max(ret, bb | (x << k))
        return ret