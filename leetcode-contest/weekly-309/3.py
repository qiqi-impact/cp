class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ret = 1
        i, j = 0, 0
        cum = [0] * 32
        
        def fine(j):
            if j == len(nums):
                return False
            for k in range(32):
                if (nums[j] & (1 << k)) and cum[k] > 0:
                    return False
            return True
        
        def tick(j, df):
            for k in range(32):
                if (nums[j] & (1 << k)):
                    cum[k] += df
        
        for i in range(len(nums)):
            if i > 0:
                tick(i-1, -1)
            while fine(j):
                tick(j, 1)
                j += 1
                ret = max(ret, j - i)
            # print(i, j, cum)
        return ret