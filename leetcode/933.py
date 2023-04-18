class RecentCounter:

    def __init__(self):
        self.q = deque()
        self.ct = 0

    def ping(self, t: int) -> int:
        self.ct += 1
        self.q.append(t)
        while 1:
            cur = self.q[0]
            if cur >= t - 3000:
                break
            self.q.popleft()
            self.ct -= 1
        return self.ct


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)