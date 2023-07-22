class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        p = [0, 0]
        for i in range(len(nums)-1, -1, -1):
            m = nums[i] % 2
            v = max(nums[i] + p[m], nums[i] + p[1-m] - x)
            p[m] = max(p[m], v)
        return p[nums[0]%2]