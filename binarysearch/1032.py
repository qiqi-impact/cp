class Solution:
    def solve(self, nums):
        left = defaultdict(int)
        right = defaultdict(int)
        for n in nums:
            right[n] += 1
        ret = 0
        for j in range(len(nums)):
            right[nums[j]] -= 1
            if nums[j]%2==0:
                ret += left[nums[j]//2] * right[nums[j]*2]
            left[nums[j]] += 1
        return ret