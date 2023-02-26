class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return ret