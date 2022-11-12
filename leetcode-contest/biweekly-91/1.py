class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        nums.sort()
        for i in range(len(nums)//2):
            s.add((nums[i] + nums[len(nums)-1-i])/2)
        return len(s)