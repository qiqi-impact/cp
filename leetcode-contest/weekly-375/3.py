class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        idx = []
        for i, x in enumerate(nums):
            if x == mx:
                idx.append(i)
        ret = 0
        ct = 0
        for i, x in enumerate(nums):
            if ct + k - 1 >= len(idx):
                break
            ret += len(nums) - idx[ct + k - 1]
            if x == mx:
                ct += 1
        return ret
        