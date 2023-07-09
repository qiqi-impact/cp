class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        d = {}
        st = 0
        for i in range(len(nums)):
            if i in d:
                st -= d[i]
            if nums[i] < st:
                return False
            if nums[i] != st:
                d[i+k] = nums[i] - st
                if i+k > len(nums):
                    return False
                st = nums[i]
        return True