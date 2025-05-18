class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            l = sum([int(x) for x in str(nums[i])])
            if l == i:
                return i
        return -1