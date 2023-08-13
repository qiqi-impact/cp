class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ret = -1
        for i in range(len(nums)):
            a = [int(x) for x in str(nums[i])]
            for j in range(i+1, len(nums)):
                b = [int(x) for x in str(nums[j])]
                if max(a) == max(b):
                    ret = max(ret, nums[i] + nums[j])
        return ret