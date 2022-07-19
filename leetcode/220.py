class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}
        for i, n in enumerate(nums):
            idx = n//(t+1)
            if idx in buckets and buckets[idx][1] >= i-k:
                return True
            buckets[idx] = (n, i)
            for q in [idx-1, idx+1]:
                if q in buckets:
                    if buckets[q][1] < i-k:
                        del buckets[q]
                    elif abs(buckets[idx][0] - buckets[q][0]) <= t:
                        return True
        return False