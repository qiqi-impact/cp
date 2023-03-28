class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d = [0] * value
        for x in nums:
            d[x%value] += 1
        md = min(d)
        ret = md * value
        for i in range(value):
            if d[i] == md:
                return ret + i