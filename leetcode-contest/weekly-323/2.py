class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ret = -1
        s = set(nums)
        for n in nums:
            cn = n
            for i in range(2, 10**5+1):
                cn *= cn
                if cn in s:
                    ret = max(ret, i)
                else:
                    break
        return ret