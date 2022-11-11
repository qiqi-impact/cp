class StockSpanner:

    def __init__(self):
        self.ms = []

    def next(self, price: int) -> int:
        cur = 1
        while self.ms and self.ms[-1][0] <= price:
            cur += self.ms[-1][1]
            self.ms.pop()
        self.ms.append((price, cur))
        return cur


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)