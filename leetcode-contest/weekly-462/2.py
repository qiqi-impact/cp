class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        ret = None
        for i in range(n):
            if nums[i] != i:
                if ret is None:
                    ret = i
                else:
                    ret &= i
        return 0 if ret is None else ret©leetcode