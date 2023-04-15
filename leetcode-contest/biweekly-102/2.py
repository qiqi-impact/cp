class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        arr = []
        mx = -inf
        cur = 0
        ret = []
        for x in nums:
            mx = max(mx, x)
            arr.append(mx + x)
            cur += arr[-1]
            ret.append(cur)
        return ret