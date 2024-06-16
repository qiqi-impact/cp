class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        md = defaultdict(int)
        ret = 0
        for x in hours:
            m = x%24
            if m == 0:
                ret += md[0]
            else:
                ret += md[24-m]
            md[m] += 1
        return ret