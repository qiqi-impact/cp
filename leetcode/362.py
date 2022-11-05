import heapq
class HitCounter:

    def __init__(self):
        self.h = []

    def hit(self, timestamp: int) -> None:
        heapq.heappush(self.h, timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.h and self.h[0] <= timestamp - 300:
            heapq.heappop(self.h)
        return len(self.h)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)