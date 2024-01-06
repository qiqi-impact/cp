class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        b = k
        for x in nums:
            b ^= x
        return bin(b).count('1')