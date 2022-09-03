class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)-1):
                if nums[i] + nums[i+1] == nums[j] + nums[j+1]:
                    return True
        return False