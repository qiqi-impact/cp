class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        top = nums[-1]
        ret = 0
        for i in range(len(nums)-2, -1, -1):
            split = (nums[i] - 1) // top
            ret += split
            top = nums[i] // (split + 1)
        return ret