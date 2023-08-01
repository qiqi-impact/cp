class Bitset:

    def __init__(self, size: int):
        self.b = [False] * size
        self.f = False
        self.ct = 0

    def at(self, idx: int) -> bool:
        r = self.b[idx]
        return not r if self.f else r

    def fix(self, idx: int) -> None:
        if self.at(idx) == True:
            return
        self.b[idx] = False if self.f else True
        self.ct += 1

    def unfix(self, idx: int) -> None:
        if self.at(idx) == False:
            return
        self.b[idx] = True if self.f else False
        self.ct -= 1

    def flip(self) -> None:
        self.f = not self.f
        self.ct = len(self.b) - self.ct

    def all(self) -> bool:
        return self.ct == len(self.b)

    def one(self) -> bool:
        return self.ct >= 1

    def count(self) -> int:
        return self.ct

    def toString(self) -> str:
        return ''.join([str(int(self.at(i))) for i in range(len(self.b))])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()