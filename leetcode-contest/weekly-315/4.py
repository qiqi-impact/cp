class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ret = 0
        i = back = 0
        mins_j, maxs_j = 0, 0
        mins_i, maxs_i = 0, 0
        for j in range(len(nums)):
            if not minK <= nums[j] <= maxK:
                mins_j, maxs_j = 0, 0
                mins_i, maxs_i = 0, 0
                i = back = j+1
                continue
            mins_j += int(nums[j] == minK)
            maxs_j += int(nums[j] == maxK)
            if mins_j >= 1 and maxs_j >= 1:
                while mins_j - (mins_i + int(nums[i] == minK)) >= 1 and maxs_j - (maxs_i + int(nums[i] == maxK)) >= 1:
                    mins_i += int(nums[i] == minK)
                    maxs_i += int(nums[i] == maxK)
                    i += 1
                ret += i + 1 - back
        return ret
        