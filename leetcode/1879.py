class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dfs(idx, taken):
            # idx = current index of nums1 that we are trying to match up
            # taken = bitmap of which elts of nums2 have been taken so far
            if idx == len(nums1):
                return 0
            ret = float('inf')
            for i in range(len(nums2)):
                if taken & (1 << i) == 0:
                    ret = min(ret, (nums1[idx] ^ nums2[i]) + dfs(idx+1, taken | (1 << i)))
            return ret
        return dfs(0, 0)
    #O(N * 2^N)