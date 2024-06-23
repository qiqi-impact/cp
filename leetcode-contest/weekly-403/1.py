class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        mn = inf
        for i in range(len(nums)//2):
            mn = min(mn, (nums[i] + nums[-i-1])/2)
        return mn