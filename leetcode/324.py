class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        l = nums[:(len(nums)+1)//2]
        r = nums[(len(nums)+1)//2:]
        lp, rp = len(l)-1, len(r)-1
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = l[lp]
                lp -= 1
            else:
                nums[i] = r[rp]
                rp -= 1