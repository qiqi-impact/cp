class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        lst = [-1] * 32
        ret = 0
        for i in range(len(nums)):
            mn, mx = -1, i-1
            for j in range(32):
                if not (nums[i] & 1 << j):
                    lst[j] = i
                if k & 1 << j:
                    mn = max(mn, lst[j])
                else:
                    mx = min(mx, lst[j] - 1)
            ret += max(0, mx - mn + 1)
        return ret