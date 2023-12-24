class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        for i in range(0, len(nums), 2):
            ret.append(nums[i+1])
            ret.append(nums[i])
        return ret