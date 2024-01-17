class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []
        self.st = 0

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.l.append(val)
        self.d[val] = len(self.l) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        idx = self.d[val]
        if idx != self.st:
            t = self.l[self.st]
            self.l[idx], self.l[self.st] = self.l[self.st], self.l[idx]
            self.d[t] = idx
        self.st += 1
        del self.d[val]
        return True

    def getRandom(self) -> int:
        idx = random.randint(self.st, len(self.l) - 1)
        return self.l[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()