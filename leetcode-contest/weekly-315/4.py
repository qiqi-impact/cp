class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        a = b = back = -1
        ret = 0
        for i in range(len(nums)):
            x = nums[i]
            if not minK <= x <= maxK:
                back = i
            if x == minK:
                a = i
            if x == maxK:
                b = i
            ret += max(0, min(a, b) - back)
        return ret