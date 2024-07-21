class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        s = [nums[i] - target[i] for i in range(len(nums))]
        n = len(nums)
        lst = 0
        ret = 0
        for x in s:
            if x > 0:
                if lst < x:
                    ret += min(x - lst, x)
            elif x < 0:
                if lst > x:
                    ret += min(lst - x, -x)
            lst = x
        return ret