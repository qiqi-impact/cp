def nondec(x):
    for i in range(1, len(x)):
        if x[i] < x[i-1]:
            return False
    return True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ct = 0
        while not nondec(nums):
            ct += 1
            mn = inf
            mni = None
            for i in range(len(nums)-1):
                a, b = nums[i], nums[i+1]
                if a + b < mn:
                    mn = a + b
                    mni = i
            nums = nums[:mni] + [mn] + nums[mni+2:]
            # print(nums)
        return ct