class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ct = 0
        ret = 0
        lst = -inf
        for x in nums:
            if x > lst:
                ct += 1
            else:
                ct = 1
            ret = max(ret, ct)
            lst = x
        ct = 0
        lst = -inf
        for x in nums:
            if x < lst:
                ct += 1
            else:
                ct = 1
            ret = max(ret, ct)
            lst = x
        return ret