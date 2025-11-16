class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n = len(nums)
        ret = -inf
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or i == k or j == k:
                        continue
                    ret = max(ret, nums[i] + nums[j] - nums[k])
        return ret