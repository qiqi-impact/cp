class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        ret = -1
        for i in range(len(nums)):
            v = nums[i]
            if i >= 2 and v < s:
                ret = v + s
            s += v
        return ret