class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        ret = -1
        s = set(nums)
        for n in nums:
            cn = n
            for i in range(2, len(nums)+10):
                cn *= cn
                if cn in s:
                    ret = max(ret, i)
                else:
                    break
        return ret