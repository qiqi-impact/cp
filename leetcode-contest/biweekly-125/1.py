class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ct = 0
        for x in nums:
            if x < k:
                ct += 1
        return ct