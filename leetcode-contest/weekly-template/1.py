class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        sm = 0
        i, j = 0, len(nums)-1
        while j > i:
            sm += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        if i == j:
            sm += nums[i]
        return sm