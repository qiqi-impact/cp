class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        li = defaultdict(int)
        for i, x in enumerate(nums):
            li[x] = i
        s = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    v = target - nums[i] - nums[j] - nums[k]
                    if v in li and li[v] > k:
                        s.add(tuple(sorted([nums[i], nums[j], nums[k], v])))
        return list(s)