from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k == 0: return False
        sl = SortedList()
        for i, n in enumerate(nums):
            idx = sl.bisect_left(n)
            for v in [idx, idx-1]:
                if 0 <= v < len(sl):
                    if abs(n - sl[v]) <= t:
                        return True
            if i - k >= 0:
                sl.discard(nums[i-k])
            sl.add(n)
        return False