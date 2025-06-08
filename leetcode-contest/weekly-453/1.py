class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l = nums[:]
        c = 0
        for i in range(n-1):
            if l[i] != 1:
                l[i] *= -1
                l[i+1] *= -1
                c += 1
        if l[-1] == 1 and c <= k:
            return True
        l = nums[:]
        c = 0
        for i in range(n-1):
            if l[i] != -1:
                l[i] *= -1
                l[i+1] *= -1
                c += 1
        if l[-1] == -1 and c <= k:
            return True
        return False