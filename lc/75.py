class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for k in range(2):
            while ptr < len(nums) and nums[ptr] == k:
                ptr += 1
            for i in range(len(nums)-1, -1, -1):
                if i <= ptr:
                    break
                if nums[i] == k:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    while ptr < len(nums) and nums[ptr] == k:
                        ptr += 1
        return nums