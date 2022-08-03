class MyCalendar:

    def __init__(self):
        self.intervals = [(float('-inf'), float('-inf')), (float('inf'), float('inf'))]
        
    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_right(self.intervals, (start, end)) - 1
        if start >= self.intervals[idx][1] and end <= self.intervals[idx+1][0]:
            self.intervals.insert(idx+1, (start, end))
            return True
        return False
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)