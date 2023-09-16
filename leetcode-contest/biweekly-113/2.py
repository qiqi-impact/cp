class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        st = (n+1)//2
        ret = n%2
        for i in range(n//2):
            if nums[i] == nums[st+i]:
                ret += 2
        return ret