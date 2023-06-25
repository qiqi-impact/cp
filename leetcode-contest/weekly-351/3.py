class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0
        ret = 1
        lst = None
        for i, x in enumerate(nums):
            if x == 1:
                if lst is not None:
                    ret *= i - lst
                    ret %= (10**9+7)
                lst = i
        return ret