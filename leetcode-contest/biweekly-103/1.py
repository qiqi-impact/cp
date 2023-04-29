class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ret = 0
        for i in range(k):
            ret += mx + i
        return ret