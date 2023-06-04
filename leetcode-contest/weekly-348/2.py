class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        a, b = None, None
        for i in range(len(nums)):
            if nums[i] == 1:
                a = i
            elif nums[i] == len(nums):
                b = i
        ret = a
        if b < a:
            ret -= 1
        ret += len(nums)-1-b
        return ret