class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        ev = defaultdict(int)
        
        for x, y in meetings:
            ev[x] += 1
            ev[y+1] -= 1
        
        st = 0
        l = None
        for k in sorted(ev.keys()):
            if st == 0:
                l = k
            st += ev[k]
            if st == 0:
                days -= k - l
        return days