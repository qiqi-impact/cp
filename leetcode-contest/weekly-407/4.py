class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        s = [nums[i] - target[i] for i in range(len(nums))]
        n = len(nums)
        lst = 0
        ret = 0
        for x in s:
            if x == 0:
                lst = 0
                continue
            elif x > 0:
                if lst >= x:
                    lst = x
                else:
                    ret += min(x - lst, x)
                    lst = x
            else:
                if lst <= x:
                    lst = x
                else:
                    ret += min(lst - x, -x)
                    lst = x
        return ret