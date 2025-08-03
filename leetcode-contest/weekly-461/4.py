class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ret = -inf
        best = [nums[0],-inf,-inf,-inf]
        for i in range(1, n):
            a, b, c, d = best
            if nums[i] > nums[i-1]:
                d = max(c, d)
                d += nums[i]
                ret = max(ret, d)
            else:
                d = -inf

            if nums[i] < nums[i-1]:
                c = max(b, c)
                c += nums[i]
            else:
                c = -inf

            if nums[i] > nums[i-1]:
                b = max(a, b)
                b += nums[i]
            else:
                b = -inf

            a = nums[i]
            best = [a, b, c, d]
        return ret
                