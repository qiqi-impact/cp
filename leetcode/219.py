class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lst = {}
        for i, n in enumerate(nums):
            if n in lst and lst[n] + k >= i:
                return True
            lst[n] = i
        return False