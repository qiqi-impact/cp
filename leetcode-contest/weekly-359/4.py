from sortedcontainers import SortedList

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        j = 0
        d = defaultdict(int)
        sl = SortedList()
        ret = 0
        for i in range(len(nums)):
            while j < len(nums):
                v = nums[j]
                if v in d:
                    sl.discard(d[v])
                d[v] += 1
                sl.add(d[v])
                j += 1
                if j-i <= sl[-1] + k:
                    ret = max(ret, sl[-1])
                else:
                    break
            d[nums[i]] -= 1
        return ret