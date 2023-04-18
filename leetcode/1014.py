class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        mx = -inf
        ret = -inf
        for i in range(len(values)):
            ret = max(ret, mx + values[i] - i)
            mx = max(mx, values[i] + i)
        return ret
