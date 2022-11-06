class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        ct = 0
        ret = []
        for n in nums:
            if n == 0:
                ct += 1
            else:
                ret.append(n)
        return ret + ([0] * ct)