class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        l = [sum([int(x) for x in str(y)]) for y in nums]
        z = sorted(zip(l, nums))
        z = [x[1] for x in z]

        pos = {}
        for i, x in enumerate(nums):
            pos[x] = i

        ret = 0
        for j in range(len(nums)):
            if nums[j] != z[j]:
                q = pos[z[j]]
                nums[j], nums[q] = nums[q], nums[j]
                pos[nums[q]], pos[nums[j]] = pos[nums[j]], pos[nums[q]]
                ret += 1
        return ret