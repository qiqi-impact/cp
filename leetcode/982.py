class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                cur = nums[i] & nums[j]
                d[cur] = d.get(cur, 0) + 1
        ret = 0
        for i in range(len(nums)):
            for c in d:
                if c & nums[i] == 0:
                    ret += d[c]
        return ret