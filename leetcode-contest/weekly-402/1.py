class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        md = defaultdict(int)
        ret = 0
        for x in hours:
            m = x%24
            ret += md[(24-m)%24]
            md[m] += 1
        return ret