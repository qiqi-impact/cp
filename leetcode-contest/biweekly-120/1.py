class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                f = 0
                cur = -inf
                for k in range(len(nums)):
                    if k < i or k > j:
                        if nums[k] <= cur:
                            f = 1
                            break
                        cur = nums[k]
                if not f:
                    ret += 1
        return ret