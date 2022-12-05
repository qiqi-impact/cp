class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        MOD = 10**6
        for i in range(len(nums)):
            nums[(nums[i]-1)%MOD] += MOD
        ret = []
        for i in range(len(nums)):
            if nums[i] >= 2*MOD:
                ret.append(i+1)
        return ret