class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ct = 0
        j = 0
        d = defaultdict(int)
        ret = 0
        for i in range(len(nums)):
            while j < len(nums) and ct < k:
                v = nums[j]
                d[v] += 1
                ct += d[v] - 1
                j += 1
            if ct >= k:
                ret += len(nums) - j + 1
            d[nums[i]] -= 1
            ct -= d[nums[i]]
        return ret