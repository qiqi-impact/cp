class FrequencyTracker:

    def __init__(self):
        self.d = defaultdict(int)
        self.inv = defaultdict(int)

    def add(self, number: int) -> None:
        self.d[number] += 1
        v = self.d[number]
        self.inv[v] += 1
        self.inv[v-1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.d[number] == 0:
            return
        self.d[number] -= 1
        v = self.d[number]
        self.inv[v] += 1
        self.inv[v+1] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.inv[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)