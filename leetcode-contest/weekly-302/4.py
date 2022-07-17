class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        g = math.gcd(*numsDivide)
        for i in range(len(nums)):
            if g%nums[i]==0:
                return i
        return -1