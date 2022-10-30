class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ct = 0
        i, j = 0, -1
        ret = 0
        for i in range(len(nums)):
            while 1:
                if j+1 == len(nums) or ct + (int)(nums[j+1]==0) >= 2:
                    break
                j += 1
                ct += (int)(nums[j] == 0)
            ret = max(ret, j - i + 1)
            ct -= (int)(nums[i] == 0)
        return ret