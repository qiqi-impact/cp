class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ct = [0, 0]
        ret = 0
        for x in arr:
            if x%2 == 0:
                ct[0] += 1
            else:
                ct[0], ct[1] = ct[1], ct[0]
                ct[1] += 1
            ret += ct[1]
            ret %= 10**9+7
        return ret