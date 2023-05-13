class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        R, C = len(nums), len(nums[0])
        nums = [sorted(x, reverse=True) for x in nums]
        ret = 0
        for j in range(C):
            mx = -inf
            for i in range(R):
                mx = max(mx, nums[i][j])
            ret += mx
        return ret