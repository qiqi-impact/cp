class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ret = 0
        for i in range(len(nums)):
            e = 0
            for j in range(i, len(nums)):
                if not (nums[j] % 2 == e and nums[j] <= threshold):
                    break
                e = 1-e
                ret = max(ret, j-i+1)
        return ret