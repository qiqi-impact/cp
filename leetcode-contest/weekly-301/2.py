class SmallestInfiniteSet:

    def __init__(self):
        self.h = []
        self.sm = 1
        self.s = set()

    def popSmallest(self) -> int:
        if self.h:
            x = heapq.heappop(self.h)
            self.s.discard(x)
            return x
        self.sm += 1
        return self.sm - 1

    def addBack(self, num: int) -> None:
        if num >= self.sm:
            return
        if num in self.s:
            return
        heapq.heappush(self.h, num)
        self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)