class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        def f(idx, a, b):
            if idx == n-1:
                return 0
            if nums1[idx] <= a and nums2[idx] <= b:
                return f(idx+1, a, b)
            elif nums2[idx] <= a and nums1[idx] <= b:
                return 1 + f(idx+1, a, b)
            else:
                return inf
        ans = min(f(0, nums1[-1], nums2[-1]), 1 + f(0, nums2[-1], nums1[-1]))
        return ans if ans < 10**9 else -1