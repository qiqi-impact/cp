class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ret = []
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                ret.append(0)
                continue
            nx = (i+nums[i])%n
            ret.append(nums[nx])
        return ret