MOD = 10**9+7

def inv(x):
    return pow(x, -1, MOD)

class Fancy:

    def __init__(self):
        self.cmult = 1
        self.add = 0
        self.vals = []

    def append(self, val: int) -> None:
        self.vals.append((val - self.add) * inv(self.cmult) % MOD)

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add *= m
        self.add %= MOD
        self.cmult *= m
        self.cmult %= MOD

    def getIndex(self, idx: int) -> int:
        if not 0 <= idx < len(self.vals):
            return -1
        return (self.vals[idx] * self.cmult + self.add) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)