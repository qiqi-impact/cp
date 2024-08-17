class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        good = [0]
        n = len(nums)
        for i in range(n-1):
            v = nums[i+1] - nums[i] != 1
            good.append(good[-1] + v)
        ret = []
        for i in range(n - k + 1):
            if k == 1:
                b = True
            else:
                b = good[i] == good[i+k-1]
            if b:
                ret.append(nums[i] + k - 1)
            else:
                ret.append(-1)
        return ret