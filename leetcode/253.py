class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ev = []
        for x, y in intervals:
            ev.append((x, 1))
            ev.append((y, -1))
        ev.sort()
        ct = 0
        mx = 0
        for x, y in ev:
            ct += y
            mx = max(mx, ct)
        return mx