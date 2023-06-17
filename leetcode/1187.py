class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def dp(idx, lst):
            if idx == len(arr1):
                return 0
            v = arr1[idx]
            ans = inf
            if v > lst:
                ans = min(ans, dp(idx+1, v))
            x = bisect.bisect_left(arr2, lst+1)
            if x != len(arr2):
                ans = min(ans, 1+dp(idx+1, arr2[x]))
            return ans
        
        v = dp(0, -1)
        return v if v != inf else -1