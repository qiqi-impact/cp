class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lst = defaultdict(int)
        p = 0
        lst[0] = -1
        for i, n in enumerate(nums):
            p += n
            p %= k
            if p in lst:
                if lst[p] <= i-2:
                    return True
            else:
                lst[p] = i
        return False