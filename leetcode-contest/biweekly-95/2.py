class DataStream:

    def __init__(self, value: int, k: int):
        self.ct = 0
        self.k = k
        self.v = value

    def consec(self, num: int) -> bool:
        if num == self.v:
            self.ct += 1
        else:
            self.ct = 0
        return self.ct >= self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)