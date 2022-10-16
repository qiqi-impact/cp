class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mx = -1
        s = set(nums)
        for x in nums:
            if x > 0 and -x in s:
                mx = max(mx, x)
        return mx
        