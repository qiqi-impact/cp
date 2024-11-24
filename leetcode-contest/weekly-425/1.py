class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ret = inf
        for x in range(l, r+1):
            for i in range(len(nums)+1-x):
                cur = 0
                for j in range(x):
                    cur += nums[i+j]
                if cur > 0:
                    ret = min(ret, cur)
        return ret if ret != inf else -1