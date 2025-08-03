class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        st = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return False
            elif st == 0:
                if nums[i] < nums[i-1]:
                    if i == 1:
                        return False
                    st += 1
            elif st == 1:
                if nums[i] > nums[i-1]:
                    st += 1
            elif st == 2:
                if nums[i] < nums[i-1]:
                    return False
        return st == 2