import random

class RandomizedSet:

    def __init__(self):
        self.ct = 0
        self.l = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.l.append(val)
        self.idx[val] = len(self.l)-1
        self.ct += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        i = len(self.l) - self.ct
        j = self.idx[val]
        v = self.l[i]
        self.idx[v] = j
        del self.idx[val]
        self.l[j] = v
        self.ct -= 1
        return True

    def getRandom(self) -> int:
        idx = random.randint(len(self.l) - self.ct, len(self.l)-1)
        return self.l[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()