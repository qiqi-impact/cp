class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ret = -1
        for i in range(n):
            df = 1
            for j in range(i+1, n):
                if nums[j] - nums[j-1] == df:
                    df = -df
                    ret = max(ret, j - i + 1)
                else:
                    break
        return ret