class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        sa = sum(nums1)
        sb = sum(nums2)
        pref = [0]
        for i in range(len(nums1)):
            pref.append(pref[-1] + nums2[i] - nums1[i])
        add_to_top = 0
        add_to_bot = 0
        mx = -1e9
        mn = 1e9
        for i in range(len(pref)-1, -1, -1):
            add_to_top = max(add_to_top, mx - pref[i])
            add_to_bot = max(add_to_bot, pref[i] - mn)
            mx = max(mx, pref[i])
            mn = min(mn, pref[i])
        return max(add_to_top + sa, add_to_bot + sb)