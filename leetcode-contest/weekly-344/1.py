class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return ret