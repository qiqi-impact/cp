class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    ret = max(ret, x ^ y)
        return ret