class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        st = 0
        ev = []
        mx = 0
        for x, y in intervals:
            ev.append((x, 1))
            ev.append((y+1, -1))
        ev.sort()
        for x, y in ev:
            st += y
            mx = max(mx, st)
        return mx