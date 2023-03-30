class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        i = 0
        tot = 0
        ret = 0
        for j in range(len(nums)):
            d[nums[j]] += 1
            tot += d[nums[j]] - 1
            while tot >= k and i < len(nums):
                tot -= d[nums[i]] - 1
                d[nums[i]] -= 1
                i += 1
            ret += i
        return ret