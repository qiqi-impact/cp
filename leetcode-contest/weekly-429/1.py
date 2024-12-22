class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = nums[::-1]
        ct = 0
        while 1:
            if len(set(nums)) == len(nums):
                return ct
            for _ in range(3):
                if nums:
                    nums.pop()
            ct += 1
        return ct
            