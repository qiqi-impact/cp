class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ret = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    ret += 1
        return ret