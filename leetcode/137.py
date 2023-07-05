class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mn = min(nums)
        for i in range(len(nums)):
            nums[i] -= mn
        ret = 0
        for i in range(34):
            cur = 1 << i
            t = 0
            for x in nums:
                if x & cur:
                    t += 1
            ret += (t%3) * cur
        return ret + mn