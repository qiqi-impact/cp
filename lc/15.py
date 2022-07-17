class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        n = len(nums)
        for i in range(n):
            s = set()
            for k in range(i+1, n):
                if -nums[i]-nums[k] in s:
                    l = [nums[i], nums[k], -nums[i]-nums[k]]
                    l.sort()
                    ret.add(tuple(l))
                s.add(nums[k])
        return list(ret)