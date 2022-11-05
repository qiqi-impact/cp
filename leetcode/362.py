class HitCounter:

    def __init__(self):
        self.l = []

    def hit(self, timestamp: int) -> None:
        self.l.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        idx = bisect.bisect_left(self.l, timestamp - 299)
        return len(self.l)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)