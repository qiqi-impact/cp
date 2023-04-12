class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ret = []
        st, ed = intervals[0]
        for x, y in intervals:
            if x > ed:
                ret.append([st, ed])
                st = x
                ed = y
            else:
                ed = max(ed, y)
        ret.append([st, ed])
        return ret