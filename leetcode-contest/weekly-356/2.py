class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0
        for i in range(len(nums)):
            x = set()
            for j in range(i, len(nums)):
                x.add(nums[j])
                if len(x) == len(s):
                    ret += 1
        return ret