class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        lst = -inf
        ct = 0
        for x in nums:
            if x - k > lst:
                lst = x - k
                ct += 1
            elif x + k > lst:
                lst += 1
                ct += 1
        return ct