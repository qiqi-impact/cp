MOD = 10**9+7

def inv(x):
    return pow(x, -1, MOD)

class Fancy:

    def __init__(self):
        self.cmult = 1
        self.mult = [(-1, 1)]
        self.add = 0
        self.vals = []

    def append(self, val: int) -> None:
        self.vals.append(val - self.add)

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add *= m
        self.add %= MOD
        self.cmult *= m
        self.cmult %= MOD
        self.mult.append((len(self.vals)-1, self.mult[-1][1] * inv(m) % MOD))

    def getIndex(self, idx: int) -> int:
        if not 0 <= idx < len(self.vals):
            return -1
        j = bisect_left(self.mult, (idx, 0)) - 1
        m = self.cmult * self.mult[j][1] % MOD
        return (self.vals[idx] * m + self.add) % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)