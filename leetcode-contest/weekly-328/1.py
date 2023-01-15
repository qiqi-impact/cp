class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        y = sum(nums)
        s = 0
        for x in nums:
            s += sum([int(c) for c in str(x)])
        return abs(s - y)